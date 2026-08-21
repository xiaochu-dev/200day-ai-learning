# Day 28 — 小项目：模拟团队协作工作流

> Week 4 Git 版本控制周 | 2026-08-13（周四）


---

## 今日目标

用脚本**模拟两名开发者的完整协作流程**：从创建分支到 PR 合并，体验真实团队开发中的 Git 工作流。

---

## 一、今天的场景

你扮演两名开发者：

```
开发者 Alice（前端）    开发者 Bob（后端）
       │                      │
       └──────────┬───────────┘
                  │
           GitHub 远程仓库
                  │
            main ← develop
```

### 工作流全貌

```
main ─────●──────────────────────●────  （只接受 develop 的 PR）
           \                    /
develop ────●────●────●────●───  （开发主线）
              \    \    \
feature/     Alice  Bob  Alice   （功能分支 → PR → 合并到 develop）
login       signup  api  style
(PR)        (PR)   (PR) (PR)
```

---

## 二、标准化协作流程

```
1. 从 develop 拉取最新代码
2. 创建功能分支 feature/xxx
3. 在分支上开发 + 提交
4. 推送到远程
5. 创建 Pull Request（develop ← feature/xxx）
6. Code Review（同事审查）
7. 修改（如需要）
8. Merge 到 develop
9. 删除功能分支
```

---

## 三、常见协作问题与解决

### 场景 1：有人比我快，develop 已经更新了

```
你的 timeline：
  拉取 develop（版本 A）→ 开发中... → 开发完成 →
  准备 PR 时发现 develop 已经变成版本 B 了

解决方案：
  git fetch origin
  git rebase origin/develop     # 把你的提交放到 develop 最新位置
  # 如果有冲突，逐个解决
  git push --force-with-lease   # （rebase 后需要 force push）
```

**为什么用 `--force-with-lease` 而不是 `--force`？**

`--force-with-lease` 更安全——它会先检查远程分支是否被人改动过，如果有人在你之后又推送了，它会拒绝 force push，防止覆盖别人的代码。

### 场景 2：PR 被要求修改

```
Reviewer: "这个变量名改成 is_active 更清晰"

做法：
  直接在 feature 分支上修改 → git add → git commit → git push
  PR 会自动更新！不需要重新创建 PR
```

### 场景 3：合并时产生冲突

```
develop 上有人改了 settings.py 的第 10 行
你的分支也改了 settings.py 的第 10 行
→ PR 显示 "This branch has conflicts that must be resolved"

解决：
  git fetch origin
  git merge origin/develop    # 合并 develop 的最新代码到你的分支
  # 解决冲突...
  git add .
  git commit
  git push
  # PR 的冲突标记会自动消失
```

---

## 四、分支命名约定（团队必备）

| 前缀 | 用途 | 示例 |
|------|------|------|
| `feature/` | 新功能 | `feature/user-login` |
| `fix/` | Bug 修复 | `fix/login-redirect` |
| `hotfix/` | 紧急修复 | `hotfix/critical-payment` |
| `refactor/` | 重构 | `refactor/auth-module` |
| `docs/` | 文档 | `docs/api-guide` |
| `chore/` | 杂项（依赖更新等） | `chore/update-deps` |

---

## 五、Commit Message 规范（团队必备）

### Conventional Commits 格式

```
<type>: <short description>

<optional body>
```

| type | 含义 |
|------|------|
| `feat` | 新功能 |
| `fix` | Bug 修复 |
| `refactor` | 重构（不改功能） |
| `docs` | 文档 |
| `test` | 测试 |
| `chore` | 杂项 |
| `style` | 格式（不影响代码逻辑） |

### 好的 vs 差的 commit message

```
✅ feat: add user login with JWT authentication
✅ fix: prevent double submit on checkout button
✅ refactor: extract validator from controller
✅ docs: add API usage examples to README

❌ update
❌ fix bug
❌ 改了点东西
❌ WIP
```

---

## 六、今日任务清单

### 脚本练习
- [ ] **运行 `Day28_team_workflow.sh`** —— 模拟两个开发者的完整协作
  - 创建"远程"裸仓库 + 初始化 develop 分支
  - Alice 克隆 → 创建 `feature/alice-login` → 开发 → push → 创建 PR
  - Bob 克隆 → 创建 `feature/bob-api` → 开发 → push → 创建 PR
  - Alice 的 PR 先合入 develop → Bob rebase develop → 解决可能的冲突 → 合入
  - 最终：两个功能都合并到 develop，develop 再合并到 main

### 手动实践
- [ ] 查看脚本中每个 `git` 命令的输出，理解每一步
- [ ] 观察冲突如何被标记和解决
- [ ] 理解 force-with-lease 比 force 安全在哪里

### 总结回顾
- [ ] 你能画出 main ← develop ← feature 的分支关系图吗？
- [ ] 分支命名规范和 commit message 规范记住了吗？
- [ ] PR → Review → Merge 的流程能说出来吗？
- [ ] rebase + force-with-lease 的使用场景？

### 英语
- [ ] VOA 精听 15 分钟

### 收尾
- [ ] 确认练习脚本执行成功
- [ ] 提交：
  ```
  cd E:\Users\MyFiles\Desktop\200day
  git add Day28/
  git commit -m "Day28: 模拟团队协作工作流——双开发者PR+rebase+merge完整流程"
  git push
  ```

### Week 4 Git 周总结
- [ ] Day 23-28 全部完成，Git 核心技能已覆盖：
  - 本地操作：add/commit/branch/merge/rebase/stash/reset/revert/cherry-pick
  - 远程操作：remote/push/pull/fetch/clone
  - 协作工具：Issues/PR/Code Review/Actions
  - 项目规范：分支命名/commit message 格式

---

## 七、提示

1. **rebase 是团队协作的关键技能**——保持历史干净，让 review 更容易
2. **PR 越小越好**——100 行的 PR 比 1000 行的 PR 更容易被 review
3. **一个 PR 只做一件事**——修 bug 和加功能分两个 PR
4. **commit message 是给未来自己看的**——三个月后你还会感谢现在好好写 message 的自己
5. 脚本中的 Alice 和 Bob 两个目录可以安全删除，不影响实际项目
