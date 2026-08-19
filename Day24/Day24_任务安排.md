# Day 24 — 远程协作：remote / push / pull / clone

> Week 4 Git 版本控制周 | 2026-08-09（周日）

---

## 今日目标

理解 Git 远程仓库的概念，掌握 push/pull/fetch/clone 等远程操作命令。了解 HTTPS 和 SSH 两种协议的区别和使用场景。

---

## 一、什么是远程仓库？

远程仓库（remote repository）是**托管在互联网或局域网上的 Git 仓库副本**。它让多人可以共享和同步代码。

```
你的电脑（本地）               GitHub/GitLab（远程）
┌──────────────┐              ┌──────────────┐
│  本地仓库     │  ← push ─→  │  远程仓库     │
│  (有完整历史)  │  ← fetch ─→ │  (也完整)     │
└──────────────┘              └──────────────┘
```

**关键认知**：Git 是**分布式**版本控制系统——每个人电脑上都有完整的仓库历史，远程仓库只是另一个副本。这和 SVN 等集中式系统完全不同。

---

## 二、远程操作核心命令

### 关联远程仓库

```bash
git remote add origin <url>     # 给远程仓库起名叫 origin（约定俗成）
git remote -v                   # 查看所有远程仓库的 URL
git remote show origin          # 查看 origin 的详细信息
```

### push（推送）

```bash
git push origin main            # 把本地 main 分支推送到 origin
git push -u origin main         # 推送 + 设置上游跟踪（之后只用 git push）
git push                        # 有上游跟踪后直接 push
git push origin --delete feature # 删除远程分支
```

**`-u` 参数的意思**：`--set-upstream` 的缩写。设置后本地分支和远程分支建立"跟踪关系"，以后 `git push` 就知道推到哪了。

### clone（克隆）

```bash
git clone <url>                 # 把远程仓库完整下载到本地
git clone <url> <folder-name>   # 下载到指定目录
```

`git clone` 做了三件事：
1. 把整个仓库下载下来
2. 自动设置 `origin` 远程
3. 自动切换到默认分支（通常是 main）

### fetch（获取）

```bash
git fetch origin                # 从远程下载所有更新，但不合并
git fetch origin main           # 只获取 main 分支的更新
```

### pull（拉取）

```bash
git pull origin main            # fetch + merge 一步完成
git pull --rebase origin main   # fetch + rebase（更干净的历史）
```

---

## 三、fetch vs pull 的区别

这是初学者最容易混淆的概念：

| 命令 | 做了什么 | 是否改变本地代码 |
|------|---------|-----------------|
| `git fetch` | 下载远程更新到本地数据库 | **否**（只下载，不合并） |
| `git pull` | `git fetch` + `git merge` | **是**（自动合并） |

**什么时候用 fetch？**

```
场景：你在写代码，想知道远程有没有更新，但不想直接合并。
```

```bash
git fetch origin        # 先把远程的更新拉下来看看
git log main..origin/main  # 看看远程有什么新提交
git diff main origin/main  # 看看具体改了什么
# 确认没问题了，再手动 merge
git merge origin/main
```

**什么时候用 pull？**

当你明确知道远程有更新，且信任这些更新可以直接合并时：

```bash
git pull origin main    # 直接 fetch + merge
```

**最佳实践**：团队协作时，多用 fetch 看清楚了再合并，别盲目 pull。

---

## 四、HTTPS vs SSH

两种连接远程仓库的协议：

| 特性 | HTTPS | SSH |
|------|-------|-----|
| 认证方式 | 用户名 + 密码 / token | SSH 密钥对 |
| 首次配置 | 简单（输密码就行） | 需生成密钥、配置公钥 |
| 代理支持 | 好（走 HTTP 代理） | 较复杂 |
| 安全性 | 依赖 token 保护 | 密钥对，更安全 |
| 推荐场景 | 新手、临时使用 | 日常开发 |

### HTTPS 配置

```bash
git clone https://github.com/用户名/仓库名.git
# 推送时输入用户名和 Personal Access Token
```

### SSH 配置（一次配置，永久免密）

```bash
# 1. 生成密钥（一路回车即可）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 2. 复制公钥
cat ~/.ssh/id_ed25519.pub

# 3. 粘贴到 GitHub → Settings → SSH and GPG keys → New SSH key
# 4. 测试连接
ssh -T git@github.com

# 5. 用 SSH 地址 clone
git clone git@github.com:用户名/仓库名.git
```

---

## 五、今日任务清单

### 核心概念理解
- [ ] `fetch` 和 `pull` 的区别是什么？
- [ ] `clone` 自动做了哪三件事？
- [ ] `-u`（--set-upstream）参数的作用
- [ ] HTTP 和 SSH 的优缺点对比

### 脚本练习
- [ ] **运行 `Day24_remote_practice.sh`** —— 模拟远程仓库的完整操作流程
  - 创建本地仓库 → 初始化"远程"仓库（用本地目录模拟）
  - `git remote add` → `git push -u` → clone 到另一个目录
  - 模拟协作：A 目录 push → B 目录 `git fetch` → 检查差异 → merge
  - B 目录 push → A 目录 `git pull`

### 英语
- [ ] VOA 精听 15 分钟

### 收尾
- [ ] 确认练习脚本执行成功
- [ ] 提交：
  ```
  cd E:\Users\MyFiles\Desktop\200day
  git add Day24/
  git commit -m "Day24: Git远程协作——remote/push/pull/fetch/clone + HTTPS vs SSH"
  git push
  ```

---

## 七、提示

1. **别盲目 pull**：先 fetch 看看远程改了什么，确认无冲突再 merge
2. **SSH 一劳永逸**：花 10 分钟配好 SSH，以后不用反复输密码
3. **`git clone` 是完整拷贝**：不只是下载代码文件，整个仓库历史都下来了
4. 脚本用本地目录模拟远程仓库（`--bare`），无需真正上传到 GitHub
