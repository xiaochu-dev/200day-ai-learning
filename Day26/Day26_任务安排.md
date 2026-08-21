# Day 26 — .gitignore / tag / git log 高级用法

> Week 4 Git 版本控制周 | 2026-08-11（周二）

---

## 今日目标

掌握三个实用技能：`.gitignore` 忽略文件的模式语法、`git tag` 标记版本、`git log` 的高级查询技巧。

---

## 一、.gitignore — 告诉 Git 忽略什么

### 为什么需要 .gitignore？

有些文件不应该提交到版本控制：
- **编译产物**：`node_modules/`、`__pycache__/`、`*.exe`
- **敏感信息**：`.env`（含密钥）、`*.pem`
- **系统文件**：`.DS_Store`（macOS）、`Thumbs.db`（Windows）
- **IDE 配置**：`.vscode/`、`.idea/`
- **本地配置**：用户偏好、日志文件

### 基本语法

```gitignore
# 注释：以 # 开头

# 忽略特定文件
secret.txt

# 忽略特定目录
node_modules/

# 通配符
*.log           # 所有 .log 文件
*.py[cod]       # .pyc / .pyo / .pyd
build/          # 任何名为 build 的目录
**/temp/        # 任意层级的 temp 目录

# 取反（不忽略）
!important.log  # important.log 不要忽略

# 只忽略根目录下的文件
/config.json    # 只忽略项目根目录的 config.json
```

### Python 项目典型 .gitignore

```gitignore
# 编译产物
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# 虚拟环境
venv/
.env/
.venv/

# 环境变量（含密钥）
.env
.env.local

# IDE
.vscode/
.idea/

# 系统文件
.DS_Store
Thumbs.db
```

### Node.js 项目典型 .gitignore

```gitignore
# 依赖
node_modules/

# 构建输出
dist/
build/
.next/

# 环境变量
.env
.env.local

# 日志
*.log
npm-debug.log*

# IDE
.vscode/
.idea/
```

### 实用技巧

```bash
# 全局 .gitignore（对所有仓库生效）
git config --global core.excludesfile ~/.gitignore_global

# 查看哪些文件被忽略了
git status --ignored

# 强制添加被忽略的文件
git add -f important.log

# 查看某个文件为什么被忽略
git check-ignore -v <file>
```

---

## 二、git tag — 标记版本

Tag 用于**给某个提交打标签**，通常标记发布版本号。

### 轻量标签（Lightweight Tag）

就是一个指向某个 commit 的指针（和分支类似，但不会移动）。

```bash
git tag v1.0.0              # 在当前 commit 打轻量标签
git tag v1.0.0 <commit>     # 在指定 commit 打标签
git tag                     # 列出所有标签
git show v1.0.0             # 查看标签详情
```

### 附注标签（Annotated Tag）

包含完整信息：打标签的人、时间、注释。

```bash
git tag -a v1.0.0 -m "正式发布 v1.0.0"     # 附注标签（推荐）
git tag -a v1.0.0 -m "描述" <commit>       # 在指定 commit 打附注标签
```

### 轻量 vs 附注

| | 轻量标签 | 附注标签 |
|---|---------|---------|
| 信息 | 只有标签名 | 含 tagger、日期、注释 |
| Git 对象 | 就是 ref 指针 | 独立的 tag 对象 |
| 推荐场景 | 临时标记 | **正式发布**（推荐） |

### 推送和删除标签

```bash
git push origin v1.0.0     # 推送单个标签
git push origin --tags     # 推送所有本地标签
git tag -d v1.0.0          # 删除本地标签
git push origin --delete v1.0.0  # 删除远程标签
```

---

## 三、git log — 高级查询技巧

### 基本用法速查

```bash
git log                      # 完整日志
git log --oneline            # 一行一条（精简）
git log --oneline -10        # 最近 10 条
git log --graph              # 显示分支图
git log --graph --oneline    # 分支图 + 精简（日常最常用）
```

### 按条件过滤

```bash
# 按作者
git log --author="用户名"
git log --author="用户名\|另一个用户名"   # 多作者

# 按时间
git log --since="2026-08-01"
git log --since="2026-08-01" --until="2026-08-07"
git log --since="1 week ago"
git log --since="yesterday"

# 按内容
git log --grep="fix"                  # 提交信息包含 fix
git log --grep="bug" --grep="fix"     # 同时包含 bug 和 fix
git log -S "function_name"            # 改动中出现了 function_name
git log -G "regex_pattern"            # 用正则搜索改动内容

# 按文件
git log -- path/to/file.py           # 查看某个文件的提交历史
git log -p -- path/to/file.py        # 查看文件每次改了什么
```

### 自定义输出格式

```bash
# 自定义格式：hash、作者、日期、提交信息
git log --format="%h - %an, %ar : %s"

# 常用占位符
# %h    → 缩略 hash
# %H    → 完整 hash
# %an   → 作者名
# %ae   → 作者邮箱
# %ad   → 日期
# %ar   → 相对日期（3 days ago）
# %s    → 提交信息标题
```

### 日常最常用的组合

```bash
# 1. 看项目全貌（最推荐）
git log --graph --oneline --all --decorate

# 2. 看"我"今天做了什么
git log --author="你的名字" --since="today" --oneline

# 3. 看 main 相比 feature 多了什么提交
git log main..feature
git log feature..main

# 4. 看某个文件是谁改的（逐行）
git blame path/to/file.py

# 5. 看两次提交之间改了什么
git diff <commit1> <commit2>
```

---

## 四、今日任务清单

### Part 1：创建 .gitignore

在 Day26 目录下创建一个**模拟项目**，包含需要忽略的各种文件，并编写对应的 `.gitignore`：

- [ ] 创建 `Day26_demo_project/` 目录，模拟一个 Python 项目
- [ ] 创建以下"垃圾"文件（不提交到 Git）：
  - `__pycache__/` 目录（放一个 `test.cpython-312.pyc`）
  - `venv/` 目录（放几个假文件）
  - `.env` 文件（假装有密钥）
  - `test.log` 文件
  - `.DS_Store` 文件
- [ ] 创建正常文件：`app.py`、`README.md`
- [ ] 编写 `.gitignore` 忽略上述垃圾文件
- [ ] 执行 `git status` 验证垃圾文件被忽略

### Part 2：打标签

在 Day26_demo_project 目录中：

- [ ] 做一次初始提交
- [ ] 打一个附注标签 `v0.1.0`："初始版本"
- [ ] 改点东西 → 提交 → 打 `v0.2.0`
- [ ] 用 `git tag` 和 `git show v0.2.0` 查看标签

### Part 3：git log 练习

在 200day 仓库中执行以下命令，观察输出：

- [ ] `git log --graph --oneline --all --decorate` — 看整体历史
- [ ] `git log --author="你的名字" --since="1 week ago" --oneline` — 看本周提交
- [ ] `git log --grep="Day" --oneline` — 搜索提交信息
- [ ] `git log -- Day01/` — 看某个目录的提交历史
- [ ] `git blame Day01/Day01_任务安排.md` — 看文件逐行归属

### 英语
- [ ] VOA 精听 15 分钟

### 收尾
- [ ] `.gitignore` 生效，`git status` 看到垃圾文件被忽略
- [ ] 标签创建成功
- [ ] git log 各命令结果理解
- [ ] 提交：
  ```
  cd E:\Users\MyFiles\Desktop\200day
  git add Day26/
  git commit -m "Day26: .gitignore模式语法 + tag轻量/附注 + git log高级查询"
  git push
  ```

---

## 五、提示

1. **.gitignore 只对未跟踪的文件生效**——已经在版本控制中的文件需要先 `git rm --cached`
2. **附注标签优于轻量标签**——正式发布一定要用 `git tag -a`
3. **git log --graph --oneline** 是你用得最多的日志命令，记住它
4. **git blame** 不是甩锅工具，是理解代码变更上下文的好帮手
5. GitHub 提供了很多预制 .gitignore 模板：[github/gitignore](https://github.com/github/gitignore)
