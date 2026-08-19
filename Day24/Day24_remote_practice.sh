#!/bin/bash
# ============================================================
# Day 24 — Git 远程协作练习脚本
# 模拟远程仓库的完整操作流程：
#   remote add → push → clone → pull → fetch + merge
#
# 运行方式：在 Git Bash 中执行
#   bash Day24_remote_practice.sh
# ============================================================
set -e

# 练习根目录
LABDIR="$(dirname "$0")/_remote_lab"
REMOTEDIR="$LABDIR/remote-repo.git"      # 模拟"远程"仓库（bare repo）
ALICEDIR="$LABDIR/alice-local"            # Alice 的本地目录
BOBDIR="$LABDIR/bob-local"                # Bob 的本地目录

echo "============================================"
echo "  Day 24 远程协作练习"
echo "============================================"

# 清理旧的练习目录
rm -rf "$LABDIR"

# ============================================================
# 第一阶段：创建"远程"仓库（用 bare 仓库模拟 GitHub）
# ============================================================
echo ""
echo ">>> [1/5] 创建"远程"仓库（bare repository）"
echo "     bare 仓库没有工作目录，只存 .git 数据，用于模拟 GitHub/GitLab"

mkdir -p "$REMOTEDIR"
cd "$REMOTEDIR"
git init --bare   # --bare：创建一个裸仓库（没有工作区，只有 .git 内容）

# ============================================================
# 第二阶段：Alice 创建本地仓库，关联远程，推送
# ============================================================
echo ""
echo ">>> [2/5] Alice：初始化本地仓库 → 关联远程 → 推送到远程"

mkdir -p "$ALICEDIR"
cd "$ALICEDIR"
git init
git config user.name "Alice"
git config user.email "alice@example.com"

# Alice 创建初始文件
echo "# 团队协作项目" > README.md
echo "这是一个示例项目" >> README.md
git add README.md
git commit -m "init: 项目初始化（Alice）"

# 关联远程仓库（origin 是约定俗成的名字，指"上游仓库"）
git remote add origin "$REMOTEDIR"
echo "远程仓库已添加："
git remote -v

# 推送到远程
# -u (--set-upstream)：设置上游跟踪，之后只用 git push/pull 即可
git push -u origin main
echo "Alice 已推送到远程仓库！"


# ============================================================
# 第三阶段：Bob clone 远程仓库，开始协作
# ============================================================
echo ""
echo ">>> [3/5] Bob：克隆远程仓库 → 开发 → 推送"

# git clone 做了三件事：
#   1. 下载整个仓库（含完整历史）
#   2. 自动把远程仓库命名为 origin
#   3. 自动切换到默认分支（main）
git clone "$REMOTEDIR" "$BOBDIR"
cd "$BOBDIR"
git config user.name "Bob"
git config user.email "bob@example.com"

# Bob 添加自己的文件
echo "Bob 的贡献" > bob-contribution.txt
git add bob-contribution.txt
git commit -m "feat: Bob 的第一个贡献"

# Bob 推送到远程
git push origin main
echo "Bob 已推送到远程仓库！"


# ============================================================
# 第四阶段：Alice fetch（获取但不合并）→ 检查 → merge
# ============================================================
echo ""
echo ">>> [4/5] Alice：fetch 远程更新 → 检查差异 → 手动合并"

cd "$ALICEDIR"

echo ""
echo "第一步：git fetch origin"
echo "  下载远程更新，但不改变本地代码"
git fetch origin

echo ""
echo "第二步：查看远程和本地的差异"
echo "  远程比本地多了这些提交："
git log main..origin/main --oneline

echo ""
echo "第三步：查看具体改了什么"
git diff main origin/main

echo ""
echo "第四步：确认无误，手动合并"
# 此时本地 main 还没有 Bob 的改动
# 需要 merge origin/main 把远程的改动合并进来
git merge origin/main

echo ""
echo "合并后 Alice 的文件列表："
ls -la


# ============================================================
# 第五阶段：Bob pull（fetch + merge 一步完成）
# ============================================================
echo ""
echo ">>> [5/5] Bob：使用 git pull 一键拉取更新"

cd "$ALICEDIR"

# Alice 再做一次改动
echo "Alice 的第二个贡献" > alice-v2.txt
git add alice-v2.txt
git commit -m "feat: Alice 的第二个贡献"
git push origin main

cd "$BOBDIR"

# Bob 用 pull 拉取
# git pull = git fetch + git merge（一步完成）
# 注意：在真实协作中建议用 fetch + 检查 + merge，而不是盲目 pull
echo ""
echo "Bob 执行 git pull（= fetch + merge 一步完成）"
git pull origin main

echo ""
echo "拉取后 Bob 的文件列表："
ls -la

echo ""
echo "Bob 仓库的提交历史："
git log --oneline --graph --all


# ============================================================
# 总结
# ============================================================
echo ""
echo "============================================"
echo "  练习完成！"
echo "  核心回顾："
echo "  1. git remote add origin <url> → 关联远程仓库"
echo "  2. git push -u origin main     → 推送并设置上游跟踪"
echo "  3. git clone <url>             → 完整下载仓库（3 件事）"
echo "  4. git fetch origin            → 下载更新，不合并（安全）"
echo "  5. git pull = fetch + merge    → 一键拉取（方便但有风险）"
echo "  6. git log main..origin/main   → 看远程比本地多了什么"
echo "  7. git diff main origin/main   → 看远程改了哪些内容"
echo ""
echo "  最佳实践：先 fetch 检查，再 merge"
echo "  练习目录: $LABDIR（可以安全删除）"
echo "============================================"
