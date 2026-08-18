# Day 22 — Git 基础

> 版本控制入门 + 词汇自测 | 2026-08-07（周四）

---

## 今日目标

1. **开发工具**：理解 Git 核心概念，掌握 7 个最常用命令，能独立完成 add/commit/push 完整工作流
2. **词汇**：Group 7 #26-50（enormous ~ complain），过关线 **20/25**

---

## 任务清单

### 开发工具（60min）

- [ ] **阅读概念**：Git 是什么、三区模型、7 个核心命令
- [ ] **动手练习** — 按下方「Git 命令清单」逐条在终端执行
- [ ] **参考脚本** — `Day22_git_commands.sh`（含注释的命令序列，不可直接执行，逐条阅读理解后手动输入）

### 英语（30min）

- [ ] **词汇自测 25 词** — `Day22_单词自测.txt`（做完发给 Claude 批改）
- [ ] VOA 精听 15 分钟

---

## 核心概念

### Git 是什么？

Git 是**分布式版本控制系统**。简单说：记录文件每次改了什么，可以随时回到任意历史版本。

**场景**：代码写了一周崩了，用 `git checkout` 一秒回到上周的正常版本。

### 三区模型

```
工作区 (Working Directory)         暂存区 (Staging Area)          仓库 (Repository)
     |                                   |                            |
   你正在编辑的文件                   git add 之后                  git commit 之后
   （改完还没 add）                 （准备提交的改动）              （永久保存在 .git 里）
```

### 7 个核心命令

| 命令 | 作用 | 示例 |
|------|------|------|
| `git config` | 配置用户名/邮箱（一次性） | `git config --global user.name "Your Name"` |
| `git init` | 初始化仓库（新建项目时用一次） | `git init` |
| `git status` | 查看当前状态（改了哪些文件） | `git status` |
| `git add` | 把改动加入暂存区 | `git add file.py` 或 `git add .` |
| `git commit` | 把暂存区的改动提交到仓库 | `git commit -m "描述信息"` |
| `git log` | 查看提交历史 | `git log --oneline` |
| `git diff` | 查看具体改了什么 | `git diff`（看未暂存的改动） |

---

## Git 命令清单（逐条手动执行）

> 这些命令在**练习目录**中执行，不会影响 200day 项目本身。

### 第一步：创建练习目录并初始化

```bash
# 在桌面创建练习目录
mkdir ~/Desktop/git-practice
cd ~/Desktop/git-practice

# 初始化 Git 仓库
git init

# 查看状态（此时应该显示 "No commits yet"）
git status
```

### 第二步：第一次提交

```bash
# 创建一个文件
echo "# Git 练习项目" > README.md
git status          # 看到 README.md 是 "Untracked"

# 加入暂存区
git add README.md
git status          # 看到 README.md 变成 "Changes to be committed"

# 提交到仓库
git commit -m "feat: 初始化项目，添加 README"
git log --oneline   # 看到一条提交记录
```

### 第三步：修改文件 + 多次提交

```bash
# 修改 README.md
echo "" >> README.md
echo "这是一个 Git 练习项目。" >> README.md

# 查看改动
git diff            # 看到具体改了什么行

# 添加并提交
git add README.md
git commit -m "docs: 添加项目描述"

# 再创建一个新文件
echo "print('Hello Git')" > hello.py
git add hello.py
git commit -m "feat: 添加 hello.py"

# 查看完整历史
git log --oneline
```

### 第四步：理解 git diff 的两种用法

```bash
# 修改 hello.py，但不 add
echo "print('Goodbye')" >> hello.py

# git diff：比较工作区 vs 暂存区（最近一次 commit）
git diff

# git diff --staged：比较暂存区 vs 仓库（由于还没 add，无输出）
git diff --staged

# add 后再看
git add hello.py
git diff             # 无输出（工作区和暂存区一致）
git diff --staged    # 看到暂存区相对于上次 commit 的改动
```

### 第五步：清理练习目录

```bash
cd ~/Desktop
rm -rf ~/Desktop/git-practice
```

---

## 常见问题

**Q：git add . 和 git add 文件名有什么区别？**
A：`git add .` 把当前目录所有改动都加入暂存区。`git add 文件名` 只加指定文件。推荐新手用 `git add 文件名` 精确控制，避免意外提交不想提交的文件（如密码、临时文件）。

**Q：commit message 写什么？**
A：本项目格式 `<type>: <简短描述>`。type 可选：feat（新功能）、fix（修bug）、docs（文档）、refactor（重构）、test（测试）。

**Q：如果 commit 写错了怎么办？**
A：`git commit --amend -m "新的描述"` 修改最近一次 commit 的描述。注意：只能修改还没 push 的 commit。

---

## 收尾

```
cd E:\Users\MyFiles\Desktop\200day
git add Day22/
git commit -m "Day22: Git基础 + 词汇 Group7 #26-50"
git push
```
