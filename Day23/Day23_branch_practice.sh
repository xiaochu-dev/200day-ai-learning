#!/bin/bash
# ============================================================
# Day 23 — Git 分支操作练习脚本
# 模拟一个 feature 分支的完整生命周期：
#   创建 → 切换 → 提交 → 切回 main → merge → 删除分支
#   并制造一个冲突，演示如何解决
#
# 运行方式：在 Git Bash 中执行
#   bash Day23_branch_practice.sh
# ============================================================
set -e  # 任何命令失败就停止

# 练习目录（放在临时目录，不污染项目）
WORKDIR="$(dirname "$0")/_branch_lab"
echo "============================================"
echo "  Day 23 分支操作练习"
echo "  工作目录: $WORKDIR"
echo "============================================"

# 清理旧的练习目录（如果存在）
rm -rf "$WORKDIR"

# ---- 第一阶段：初始化仓库 ----
echo ""
echo ">>> [1/6] 初始化 Git 仓库"
# 创建一个新目录，初始化 Git 仓库
mkdir -p "$WORKDIR"
cd "$WORKDIR"
git init
# 配置本地用户名和邮箱（仅对本练习仓库生效）
git config user.name "Student"
git config user.email "student@example.com"

# 创建第一个文件并提交到 main 分支
echo "# 项目说明" > README.md
echo "版本 v1.0" >> README.md
git add README.md
git commit -m "init: 项目初始化，创建 README"

echo ""
echo "当前状态："
git log --oneline


# ---- 第二阶段：创建 feature 分支并开发 ----
echo ""
echo ">>> [2/6] 创建 feature/add-greeting 分支"
# 创建并切换到新分支（等价于 git branch + git checkout）
git switch -c feature/add-greeting
# 验证当前所在分支
echo "当前分支: $(git branch --show-current)"

# 在分支上创建新文件
cat > greeting.py << 'PYEOF'
def say_hello(name):
    """打招呼"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(say_hello("World"))
PYEOF

# 暂存并提交
git add greeting.py
git commit -m "feat: 添加 greeting 模块"

# 再做一个提交（修改 README）
echo "" >> README.md
echo "## 功能列表" >> README.md
echo "- 问候功能" >> README.md
git add README.md
git commit -m "docs: 更新 README 功能列表"

echo ""
echo "feature 分支提交历史："
git log --oneline


# ---- 第三阶段：切回 main 并合并（Fast-forward） ----
echo ""
echo ">>> [3/6] 切回 main 并合并 feature 分支"
# 切换回 main 分支
git switch main

# 合并 feature 分支
# 因为 main 在切出后没有新提交，Git 会执行 Fast-forward 合并
# Fast-forward：直接把 main 指针移到 feature 的最新提交
# 不会产生额外的 merge commit（历史是一条直线）
echo ""
echo "注意：这次是 Fast-forward 合并（main 没有新提交）"
git merge feature/add-greeting

echo ""
echo "合并后 main 的提交历史："
git log --oneline


# ---- 第四阶段：删除已合并的分支 ----
echo ""
echo ">>> [4/6] 删除 feature 分支"
# -d 是安全删除：只有分支已合并才会删除，否则报错
# -D 是强制删除：不管是否合并都删除
git branch -d feature/add-greeting
echo "剩余分支："
git branch


# ---- 第五阶段：制造合并冲突 ----
echo ""
echo ">>> [5/6] 制造并解决合并冲突"
echo "     模拟场景：两个人同时改了同一个文件的同一行"

# 创建 feature/fix-greeting 分支
git switch -c feature/fix-greeting

# 修改 greeting.py 的内容（改动第 3 行）
cat > greeting.py << 'PYEOF'
def say_hello(name):
    """向用户打招呼"""
    return f"Hi, {name}!"  # Alice 改成了 Hi

if __name__ == "__main__":
    print(say_hello("World"))
PYEOF
git add greeting.py
git commit -m "fix: 把 Hello 改成 Hi（Alice 的版本）"

# 切回 main，也修改同一行
git switch main

cat > greeting.py << 'PYEOF'
def say_hello(name):
    """输出问候语"""
    return f"Hello there, {name}!"  # Bob 改成了 Hello there

if __name__ == "__main__":
    print(say_hello("World"))
PYEOF
git add greeting.py
git commit -m "fix: 把问候语改得更友好（Bob 的版本）"

# 尝试合并 feature/fix-greeting → 会产生冲突！
echo ""
echo "尝试合并 feature/fix-greeting..."
echo "预期：产生合并冲突！（两个分支改了同一行）"
if git merge feature/fix-greeting 2>/dev/null; then
    echo "意外：没有冲突"
else
    echo ""
    echo "========== 冲突发生了！文件内容如下 =========="
    echo "  <<<<<<< HEAD        → main 分支的内容（Bob 的版本）"
    echo "  =======             → 分隔线"
    echo "  >>>>>>> feature/... → feature 分支的内容（Alice 的版本）"
    echo ""
    cat greeting.py
    echo ""
    echo "==============================================="
fi


# ---- 第六阶段：手动解决冲突 ----
echo ""
echo ">>> [6/6] 解决冲突"
echo "     我们手动合并两种改动：保留两边的优点"

# 手动写入合并后的内容（去掉冲突标记，综合两边）
cat > greeting.py << 'PYEOF'
def say_hello(name):
    """向用户输出问候语"""
    return f"Hi there, {name}!"  # 综合了 Hi 和 there

if __name__ == "__main__":
    print(say_hello("World"))
PYEOF

# 标记冲突已解决
git add greeting.py

# 完成合并提交
git commit -m "merge: 解决冲突——综合 Alice 和 Bob 的问候语改动"

echo ""
echo "冲突已解决！最终文件内容："
cat greeting.py

echo ""
echo "最终提交历史（包含 merge commit）："
git log --oneline --graph


# ---- 收尾：删除分支 ----
echo ""
echo ">>> 清理：删除 feature/fix-greeting 分支"
git branch -d feature/fix-greeting
echo "剩余分支："
git branch


echo ""
echo "============================================"
echo "  练习完成！"
echo "  核心回顾："
echo "  1. git switch -c <name>  → 创建并切换分支"
echo "  2. git merge <branch>    → 合并分支"
echo "  3. Fast-forward 合并      → main 没新提交时直接移动指针"
echo "  4. 三方合并               → 两边都有新提交时产生 merge commit"
echo "  5. 冲突标记 <<< / === / >>> → 手动编辑 + git add + git commit"
echo "  6. git branch -d <name>  → 安全删除已合并的分支"
echo ""
echo "  练习目录: $WORKDIR（可以安全删除）"
echo "============================================"
