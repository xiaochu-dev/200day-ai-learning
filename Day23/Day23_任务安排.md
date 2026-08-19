# Day 23 — 分支操作：branch / merge / 冲突解决

> Week 4 Git 版本控制周 | 2026-08-08（周六）

---

## 今日目标

掌握 Git 分支的核心操作：创建、切换、合并、删除分支，理解**冲突产生的原因和解决方法**。了解 Git Flow 分支策略的基本思想。

---

## 一、为什么需要分支？

分支是 Git 最强大的功能之一。它让你可以**在不影响主线代码的情况下**开发新功能、修复 bug、做实验。

```
            main（稳定版，可随时发布）
             │
    ┌───  ← 你在 main 上继续开发
    │
    └─── feature/login ← 同时，在分支上开发登录功能
```

**没有分支的痛苦**：所有代码混在一条线上，改到一半不敢提交，也不敢切换任务。

**有分支后**：一个任务一个分支，互不干扰，做完合并回去。

---

## 二、分支的本质

分支本质上就是一个**指向某个 commit 的可移动指针**。

```
main → c1 ← c2 ← c3（HEAD → main）
                          ↑ HEAD 指向当前分支
```

当你创建新分支 `feature`，Git 只是新建了一个指针指向当前位置：

```
main → c1 ← c2 ← c3（HEAD → main, feature）
```

在 feature 上提交新代码后：

```
main → c1 ← c2 ← c3
                  ← c4 ← c5（HEAD → feature）
```

---

## 三、核心命令

### 查看分支

```bash
git branch          # 列出本地分支，* 标记当前分支
git branch -a       # 列出所有分支（含远程）
git branch -v       # 列出分支 + 最后一次提交
```

### 创建与切换

```bash
git branch <name>       # 创建分支（但不切换）
git switch <name>       # 切换到已有分支（Git 2.23+，推荐）
git checkout <name>     # 切换到已有分支（旧命令，也能用）
git switch -c <name>    # 创建并切换到新分支（推荐）
git checkout -b <name>  # 创建并切换到新分支（旧命令）
```

**switch vs checkout**：`checkout` 一个命令做了太多事（切换分支、恢复文件、创建分支），容易混淆。Git 2.23+ 引入了 `switch`（切换分支）和 `restore`（恢复文件），职责更清晰。

### 合并

```bash
git switch main         # 先切到目标分支
git merge feature       # 把 feature 的改动合并到当前分支
```

合并有两种模式：

| 合并方式 | 条件 | 结果 |
|---------|------|------|
| **Fast-forward** | main 没有新提交 | 直接把 main 指针移到 feature 最新提交 |
| **三方合并** | 两边都有新提交 | 生成一个 merge commit，有两个 parent |

### 删除分支

```bash
git branch -d feature       # 安全删除（已合并才删）
git branch -D feature       # 强制删除（不管是否合并）
```

---

## 四、合并冲突（Merge Conflict）

### 什么时候产生冲突？

当两个分支**修改了同一个文件的同一行**时，Git 无法自动决定保留哪个版本。

```
main 分支：   print("Hello World")    ← A 改了这行
feature 分支：print("Hello Git")      ← B 也改了这行
                                    ↓ 合并时：冲突！
```

### 冲突标记

冲突文件会被 Git 标记成这样：

```
<<<<<<< HEAD           ← 当前分支（main）的内容
print("Hello World")
=======                ← 分隔线
print("Hello Git")     ← 被合并分支（feature）的内容
>>>>>>> feature
```

### 解决冲突步骤

1. **打开冲突文件**，找到 `<<<<<<<` / `=======` / `>>>>>>>` 标记
2. **决定保留什么**：保留一个、两个都保留、或者重新写
3. **删除冲突标记**，保留最终内容
4. **git add <file>**：标记为已解决
5. **git commit**：完成合并

### 避免大冲突的方法

- **小步提交**：每次改动尽量小，频繁 merge 回 main
- **拉取最新代码**：merge 前先 `git pull`，确保本地是最新
- **沟通**：团队成员不要同时改同一个文件

---

## 五、分支策略：Git Flow 简介

一种经典的分支管理模型，适合有固定发布周期的项目：

```
main     ──●────────────●──────────●──  （生产环境，只接受 merge）
           \          /          /
develop  ───●──●──●──●──●──●──●──  （开发主线）
              \    /    \
feature/A  ───●──●       （功能分支，从 develop 分出，合并回 develop）
                 \
hotfix    ────────●──      （紧急修复，从 main 分出，合并回 main + develop）
```

| 分支类型 | 用途 | 从哪来 | 合到哪去 |
|---------|------|--------|---------|
| `main` | 生产环境代码 | - | - |
| `develop` | 开发主线 | main | main |
| `feature/*` | 新功能开发 | develop | develop |
| `hotfix/*` | 紧急修复 | main | main + develop |
| `release/*` | 发布准备 | develop | main + develop |

**简单项目不需要全套 Git Flow**。个人项目用 `main + feature` 分支就够了。

---

## 六、今日任务清单

### 核心概念理解
- [ ] 分支的本质是什么？（一个可移动的指针）
- [ ] Fast-forward 合并 vs 三方合并的区别
- [ ] 冲突产生的原因和解决步骤
- [ ] Git Flow 的 5 种分支类型及用途

### 脚本练习
- [ ] **运行 `Day23_branch_practice.sh`** —— 模拟一个 feature 分支的完整生命周期
  - 创建仓库 → 创建 feature 分支 → 切换 → 提交 → 切回 main → merge → 删除分支
  - 制造一个冲突 → 手动解决
  - 脚本中用**注释说明每一步的作用**，先读懂再运行

### 英语
- [ ] VOA 精听 15 分钟

### 收尾
- [ ] 确认练习脚本执行成功
- [ ] 提交：
  ```
  cd E:\Users\MyFiles\Desktop\200day
  git add Day23/
  git commit -m "Day23: Git分支操作——branch/merge/冲突解决/Git Flow"
  git push
  ```

---

## 七、提示

1. **运行脚本前先确保 Git Bash 可用**（Windows 下 `git-bash.exe Day23_branch_practice.sh`）
2. **merge 冲突不可怕**——它只是 Git 告诉你"这两个改动用了我无法自动判断，你来决定"
3. **养成习惯**：开发新功能前先 `git pull`，减少后续冲突的可能性
4. 脚本创建的临时仓库可以安全删除，不影响实际项目
