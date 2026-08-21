# Day 25 — Git 进阶：stash / rebase / cherry-pick / reset / revert

> Week 4 Git 版本控制周 | 2026-08-10（周一）

---

## 今日目标

掌握 5 个 Git 进阶操作的**使用场景和区别**：stash（暂存现场）、rebase（整理历史）、cherry-pick（精确摘取）、reset（撤销提交）、revert（安全撤销）。

---

## 一、git stash — 临时保存工作现场

### 使用场景

你正在开发功能 A，突然被叫去修复紧急 bug B。当前代码改了一半还不能提交，怎么办？

```bash
git stash           # 把当前工作区和暂存区的改动"藏"起来
git switch main     # 切到 main 去修复 bug
git switch feature  # 修完回来
git stash pop       # 恢复刚才藏的改动，继续开发
```

### stash 的本质

Git 把你的改动存到一个**特殊的"stash 栈"**上，然后让工作区回到干净状态。

```bash
git stash           # 压入 stash 栈
git stash list      # 查看 stash 列表
git stash pop       # 弹出最近一个 stash（恢复 + 删除）
git stash apply     # 恢复最近一个 stash（保留不删）
git stash drop      # 删除最近一个 stash
git stash pop stash@{1}  # 恢复指定的 stash
```

### 常见用法

```bash
# 把未跟踪的新文件也一起 stash
git stash -u

# 给 stash 加个名字（推荐）
git stash push -m "登录功能做了一半"

# 查看 stash 里改了什么
git stash show -p
```

---

## 二、git rebase — 整理提交历史

### 使用场景

你的 feature 分支开发了 3 天，main 已经往前走了很多。现在要把 feature 合并回 main：

```
合并前：
main  → A → B → C → D
              ↘
feature → E → F → G

方案 1（merge）：生成一个 merge commit
main  → A → B → C → D → M（merge commit）
              ↘         ↗
feature → E → F → G

方案 2（rebase）：把 feature 的提交"搬"到 main 最新处
main  → A → B → C → D
                      ↘
feature       → E' → F' → G'

rebase 后的历史是一条直线，更加清晰。
```

### rebase 命令

```bash
git switch feature
git rebase main        # 把 feature 的提交"重放"到 main 的最新位置
```

### rebase 过程

```
1. 找到 feature 和 main 的共同祖先（B）
2. 把 E、F、G 三个提交"暂时取下来"
3. 把 feature 指针移到 main 最新（D）
4. 把 E、F、G 一个个"重放"到 D 后面
5. 如果有冲突，逐个解决（比 merge 更细粒度）
```

### 交互式 rebase（更强大）

```bash
git rebase -i HEAD~3   # 整理最近 3 个提交
```

可以做的事：
- `pick`：保留这个提交
- `squash`：合并到上一个提交
- `reword`：改提交信息
- `drop`：删除这个提交
- `edit`：停下来让你修改

### rebase 黄金法则

> **不要 rebase 已经推送到远程的公共分支！**

原因：rebase 会重写提交历史（commit hash 会变），如果你 rebase 了别人已经拉取的提交，别人的历史和你的就对不上了。

---

## 三、git cherry-pick — 精确摘取一个提交

### 使用场景

你在 feature 分支上写了工具函数，另一个分支也需要这个函数，但不想合并整个 feature 分支。

```bash
git cherry-pick <commit-hash>    # 把指定 commit 的改动"摘"到当前分支
```

```
main  → A → B → C
              ↘
feature → D → E

# 在 main 上执行：git cherry-pick E
# 结果：main 上多了 E 的改动（新的提交 E'），但不需要合并整个 feature
```

### 常见用途

1. **跨分支搬运 bug 修复**：在 hotfix 上修好了 bug，cherry-pick 回 develop
2. **选择性地合并功能**：只需要 feature 中的某个工具函数
3. **恢复丢失的提交**：commit 被误删了，但从 reflog 找到 hash 后 cherry-pick 回来

---

## 四、git reset — 撤销提交（改历史）

### 三种模式

```bash
# 回到某个提交（三种力度）
git reset --soft <commit>    # 只移动 HEAD，改动保留在暂存区
git reset --mixed <commit>   # 移动 HEAD + 清空暂存区，改动保留在工作区（默认）
git reset --hard <commit>    # 移动 HEAD + 清空暂存区 + 丢弃工作区改动（危险！）
```

### 一张图理解三种 reset

```
工作目录          暂存区            仓库（HEAD）
  ???              ???               ← HEAD 移到这里
  ↑                ↑                    ↑
--hard 丢弃      --mixed 放工作区     --soft 放暂存区（可重新 commit）
```

```
例子：你提交了 3 次，想撤销最近 2 次

初始状态：
A → B → C（HEAD）    ← HEAD 在 C

git reset --soft HEAD~2：
A（HEAD）             ← HEAD 回到 A
B 和 C 的改动在暂存区，可以重新 commit（比如合成一个提交）

git reset --mixed HEAD~2：
A（HEAD）             ← HEAD 回到 A
B 和 C 的改动在工作区（未暂存），需要 git add 再 commit

git reset --hard HEAD~2：
A（HEAD）             ← HEAD 回到 A
B 和 C 的改动全部丢弃 ← 危险！无法恢复（除非有 reflog）
```

### 安全建议

| 场景 | 推荐命令 |
|------|---------|
| 只是想撤销 commit 但保留改动 | `git reset --soft HEAD~1` |
| 撤销 commit 和 add | `git reset --mixed HEAD~1` |
| 彻底放弃所有改动 | `git reset --hard HEAD~1`（三思！） |
| 已经 push 到远程 | **不要用 reset！用 revert！** |

---

## 五、git revert — 安全撤销（不改历史）

### reset vs revert

| | reset | revert |
|---|-------|--------|
| 原理 | 移动 HEAD 指针到旧位置 | 创建一个**新的反向提交** |
| 历史 | 改写历史（旧提交"消失"） | 保留完整历史 |
| 已推送后能用？ | **不能**（会让别人冲突） | **能**（安全） |
| 危险程度 | 中~高 | 低 |

### revert 用法的

```bash
git revert <commit-hash>     # 撤销指定 commit，生成一个新 commit
git revert HEAD              # 撤销最近一次提交
```

```
原始：A → B → C（C 有个 bug）
git revert C：
      A → B → C → C'（C' 是 C 的反操作，文件回到 B 的状态）
```

**为什么 revert 安全？**因为它不删除任何提交，只是在后面加一个新的"撤销提交"。任何时候都能回到任何历史状态。

---

## 六、各命令使用场景速查表

| 场景 | 命令 | 一句话 |
|------|------|--------|
| 临时切换分支，不想提交 | `git stash` | 把改动"藏"起来 |
| 整理本地提交历史 | `git rebase -i` | 让历史变干净 |
| 同步 main 最新代码 | `git rebase main` | 让分支"搬家"到最新 |
| 从别的分支拿一个提交 | `git cherry-pick` | 精确"摘"一个 commit |
| 撤销本地提交（保留改动） | `git reset --soft` | commit 没了，代码还在 |
| 撤销已推送的提交 | `git revert` | 新增一个反向提交 |

---

## 七、今日任务清单

### 核心概念理解
- [ ] stash 的使用场景（切换任务时暂存改动）
- [ ] merge vs rebase 的区别（merge 保留分支历史，rebase 整理成直线）
- [ ] reset 三种模式（--soft / --mixed / --hard）的区别
- [ ] reset vs revert（能不能用于已推送的提交）
- [ ] cherry-pick 的使用场景

### 脚本练习
- [ ] **运行 `Day25_advanced_practice.sh`** —— 分 5 个小实验
  1. stash：保存工作 → 切换分支 → 恢复
  2. rebase：feature 分支 rebase 到 main
  3. cherry-pick：挑一个 commit 到另一个分支
  4. reset 三种模式：分别演示 --soft / --mixed / --hard 的区别
  5. revert：撤销一个已推送的提交

### 英语
- [ ] VOA 精听 15 分钟

### 收尾
- [ ] 确认练习脚本执行成功
- [ ] 提交：
  ```
  cd E:\Users\MyFiles\Desktop\200day
  git add Day25/
  git commit -m "Day25: Git进阶——stash/rebase/cherry-pick/reset/revert 场景与区别"
  git push
  ```

---

## 八、提示

1. **rebase 黄金法则**：只 rebase 还没推送的本地提交
2. **--hard 很危险**：执行前确认没有未保存的改动，或者先 stash
3. **cherry-pick 会生成新 hash**：同一个改动在不同分支上有不同的 commit ID
4. **实在误删了**：`git reflog` 可以找回"丢失"的提交（30 天内）
