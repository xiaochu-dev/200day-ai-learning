#!/bin/bash
# ============================================================
# Day 25 — Git 进阶操作练习脚本
# 5 个实验：
#   1. stash    — 临时保存工作现场
#   2. rebase   — 整理分支历史
#   3. cherry-pick — 精确摘取一个提交
#   4. reset    — 三种模式（--soft / --mixed / --hard）
#   5. revert   — 安全撤销已推送的提交
#
# 运行方式：在 Git Bash 中执行
#   bash Day25_advanced_practice.sh
# ============================================================
set -e

LABDIR="$(dirname "$0")/_advanced_lab"
rm -rf "$LABDIR"

echo "============================================"
echo "  Day 25 Git 进阶操作练习"
echo "============================================"

# ============================================================
# 实验 1: git stash — 临时保存工作现场
# ============================================================
echo ""
echo "========== 实验 1: git stash =========="
echo "场景：正在开发功能，突然需要切到 main 修 bug"

mkdir -p "$LABDIR/exp1-stash"
cd "$LABDIR/exp1-stash"
git init
git config user.name "Student"
git config user.email "student@example.com"

# 初始提交
echo "console.log('app started')" > app.js
git add app.js
git commit -m "init: 创建 app.js"

# 模拟"开发到一半"的状态：修改了文件但还没提交
echo "console.log('feature in progress...')" >> app.js

echo "当前工作区状态（有未提交的改动）："
git status --short

# stash：把改动藏起来
echo ""
echo "执行 git stash：把当前改动保存到 stash 栈"
git stash push -m "功能开发到一半：添加了 feature log"

echo "stash 之后工作区变干净了："
git status --short

# 现在可以自由切换分支
echo ""
echo "现在可以安全地切换到其他分支去修 bug 了..."
echo "修完 bug 再回来..."

# 恢复 stash
echo ""
echo "执行 git stash pop：恢复之前保存的改动"
git stash pop

echo "恢复后工作区状态："
git status --short

echo ""
echo "stash 栈现在是空的："
git stash list || echo "(空)"


# ============================================================
# 实验 2: git rebase — 整理分支历史
# ============================================================
echo ""
echo "========== 实验 2: git rebase =========="
echo "场景：feature 分支开发期间，main 已经前进了"

mkdir -p "$LABDIR/exp2-rebase"
cd "$LABDIR/exp2-rebase"
git init
git config user.name "Student"
git config user.email "student@example.com"

# main 的初始提交
echo "# Main v1" > README.md
git add README.md
git commit -m "init: main 初始提交"

# 切换到 feature 分支
git switch -c feature/rebase-demo

echo "function login() { return 'ok'; }" > auth.js
git add auth.js
git commit -m "feat: 添加登录功能（提交 1/3）"

echo "function logout() { return 'ok'; }" >> auth.js
git add auth.js
git commit -m "feat: 添加登出功能（提交 2/3）"

echo "function checkAuth() { return true; }" >> auth.js
git add auth.js
git commit -m "feat: 添加权限检查（提交 3/3）"

echo ""
echo "feature 分支的提交（3 个提交）："
git log --oneline

# 模拟 main 前进了
git switch main
echo "# Main v2" >> README.md
echo "新的功能说明" >> README.md
git add README.md
git commit -m "docs: main 分支也前进了（模拟其他同事的提交）"

echo ""
echo "rebase 前的情况（main 和 feature 分叉了）："
git log --oneline --graph --all

# rebase：把 feature 的提交搬到 main 最新位置
echo ""
echo "执行 git rebase main：把 feature 的 3 个提交'搬'到 main 最新处"
git switch feature/rebase-demo
git rebase main

echo ""
echo "rebase 后的情况（历史变成一条直线了）："
git log --oneline --graph --all

echo ""
echo "对比 merge 和 rebase："
echo "  merge  → 产生 merge commit，保留'分叉'形状"
echo "  rebase → 提交被'重放'到 main 最新处，历史呈直线"


# ============================================================
# 实验 3: git cherry-pick — 精确摘取一个提交
# ============================================================
echo ""
echo "========== 实验 3: git cherry-pick =========="
echo "场景：从其他分支精确'摘'一个提交过来"

mkdir -p "$LABDIR/exp3-cherrypick"
cd "$LABDIR/exp3-cherrypick"
git init
git config user.name "Student"
git config user.email "student@example.com"

# main 分支
echo "# Main" > README.md
git add README.md
git commit -m "init: main 初始提交"

# 创建 feature/tools 分支，开发了 3 个工具函数
git switch -c feature/tools

echo "def add(a, b): return a + b" > utils.py
git add utils.py
git commit -m "feat: 添加 add 函数"

echo "def subtract(a, b): return a - b" >> utils.py
git add utils.py
git commit -m "feat: 添加 subtract 函数"

echo "def multiply(a, b): return a * b" >> utils.py
git add utils.py
git commit -m "feat: 添加 multiply 函数"

# 回到 main，只需要 add 函数（第一个提交）
git switch main

# cherry-pick：只拿第一个提交
ADD_COMMIT=$(git log feature/tools --oneline | tail -1 | cut -d' ' -f1)
echo ""
echo "main 上只需要 add 函数，执行 cherry-pick："
echo "  目标提交: $ADD_COMMIT"
git cherry-pick "$ADD_COMMIT"

echo ""
echo "cherry-pick 后 main 的文件内容："
cat utils.py
echo ""
echo "只有 add 函数，subtract 和 multiply 没有过来！"


# ============================================================
# 实验 4: git reset — 三种模式的区别
# ============================================================
echo ""
echo "========== 实验 4: git reset 三种模式 =========="
echo "场景：理解 --soft / --mixed / --hard 的区别"

# --- 4a: reset --soft ---
echo ""
echo "--- 4a: git reset --soft ---"
echo "  --soft 只移动 HEAD，暂存区和工作区都不动"

mkdir -p "$LABDIR/exp4-reset-soft"
cd "$LABDIR/exp4-reset-soft"
git init
git config user.name "Student"
git config user.email "student@example.com"

echo "v1" > file.txt
git add file.txt
git commit -m "v1"
echo "v2" >> file.txt
git add file.txt
git commit -m "v2"
echo "v3" >> file.txt
git add file.txt
git commit -m "v3"

echo "重置前文件内容（v1+v2+v3）："
cat file.txt

# --soft：HEAD 回到 v1，但 v2+v3 的改动留在暂存区
git reset --soft HEAD~2

echo ""
echo "git reset --soft HEAD~2 后："
echo "  暂存区状态："
git status --short
echo "  文件内容（v2 和 v3 的改动还在文件里）："
cat file.txt
echo "  说明：--soft 不丢代码，v2+v3 改动可重新 commit"

# --- 4b: reset --mixed ---
echo ""
echo "--- 4b: git reset --mixed（默认）---"
echo "  --mixed 移动 HEAD + 清空暂存区，改动放入工作区"

mkdir -p "$LABDIR/exp4-reset-mixed"
cd "$LABDIR/exp4-reset-mixed"
git init
git config user.name "Student"
git config user.email "student@example.com"

echo "v1" > file.txt
git add file.txt
git commit -m "v1"
echo "v2" >> file.txt
git add file.txt
git commit -m "v2"

# --mixed（默认行为）
git reset --mixed HEAD~1

echo ""
echo "git reset --mixed HEAD~1 后："
echo "  暂存区状态（清空了）："
git status --short
echo "  文件内容（v2 改动在工作区，但未暂存）："
cat file.txt
echo "  说明：--mixed 退回了 add 操作，改动还在，需重新 add+commit"

# --- 4c: reset --hard ---
echo ""
echo "--- 4c: git reset --hard（危险！）---"
echo "  --hard 全部丢弃：移动 HEAD + 清空暂存区 + 丢弃工作区改动"

mkdir -p "$LABDIR/exp4-reset-hard"
cd "$LABDIR/exp4-reset-hard"
git init
git config user.name "Student"
git config user.email "student@example.com"

echo "v1" > file.txt
git add file.txt
git commit -m "v1"
echo "v2" >> file.txt
git add file.txt
git commit -m "v2"

# --hard：回到 v1，v2 的改动彻底丢弃
git reset --hard HEAD~1

echo ""
echo "git reset --hard HEAD~1 后："
echo "  文件内容（只剩下 v1）："
cat file.txt
echo "  提交历史（v2 消失了）："
git log --oneline
echo "  说明：--hard 彻底丢弃改动，无法通过 git 恢复（除非 reflog）"


# ============================================================
# 实验 5: git revert — 安全撤销
# ============================================================
echo ""
echo "========== 实验 5: git revert =========="
echo "场景：线上有个 bug commit，需要安全撤销"

mkdir -p "$LABDIR/exp5-revert"
cd "$LABDIR/exp5-revert"
git init
git config user.name "Student"
git config user.email "student@example.com"

# 正常提交
echo "print('hello')" > app.py
git add app.py
git commit -m "feat: 添加问候功能"

# bug 提交：把 print 改成了错误的值
echo "print('BUG!!!!!')" > app.py
git add app.py
git commit -m "feat: 更新问候语（引入 bug！）"
BUG_COMMIT=$(git log --oneline -1 | cut -d' ' -f1)

echo ""
echo "当前文件内容（含有 bug）："
cat app.py

# revert：撤销 bug 提交（生成一个新的反向提交）
echo ""
echo "执行 git revert：撤销 bug 提交（生成一个新的反向提交）"
git revert --no-edit HEAD  # --no-edit 跳过编辑提交信息的步骤

echo ""
echo "revert 后文件内容（回到 hello）："
cat app.py

echo ""
echo "提交历史（保留了 bug commit + 新增了 revert commit）："
git log --oneline

echo ""
echo "对比 reset vs revert："
echo "  reset  → 直接删除历史（已推送后不能用，会破坏协作）"
echo "  revert → 新增反向提交（安全，任何时候都能用）"


# ============================================================
# 总结
# ============================================================
echo ""
echo "============================================"
echo "  练习完成！"
echo ""
echo "  速查表："
echo "  ┌──────────────┬────────────────────────────────┐"
echo "  │ stash        │ 临时藏起改动，切换分支          │"
echo "  │ rebase       │ 整理提交到一条直线              │"
echo "  │ cherry-pick  │ 从别的分支挑一个 commit          │"
echo "  │ reset --soft │ 撤销 commit，改动回暂存区        │"
echo "  │ reset --mixed│ 撤销 commit 和 add              │"
echo "  │ reset --hard │ 全部丢弃（危险！）               │"
echo "  │ revert       │ 新增反向提交（安全撤销）         │"
echo "  └──────────────┴────────────────────────────────┘"
echo ""
echo "  练习目录: $LABDIR（可以安全删除）"
echo "============================================"
