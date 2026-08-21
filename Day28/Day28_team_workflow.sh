#!/bin/bash
# ============================================================
# Day 28 — 模拟团队协作工作流脚本
# 模拟两名开发者（Alice & Bob）在 GitHub Flow 下的完整协作：
#   main ← develop ← feature/xxx
#                               ↓
#                         PR → code review → merge
#
# 运行方式：在 Git Bash 中执行
#   bash Day28_team_workflow.sh
# ============================================================
set -e

LABDIR="$(dirname "$0")/_team_lab"
REMOTE="$LABDIR/remote-repo.git"     # 模拟 GitHub 远程仓库
ALICE="$LABDIR/alice-workspace"      # Alice 的工作目录
BOB="$LABDIR/bob-workspace"          # Bob 的工作目录

echo "============================================"
echo "  Day 28 团队协作工作流模拟"
echo "============================================"

rm -rf "$LABDIR"

# ============================================================
# 0. 初始化远程仓库 + develop 分支
# ============================================================
echo ""
echo ">>> [0] 初始化远程仓库（bare），创建 develop 分支"

mkdir -p "$REMOTE"
cd "$REMOTE"
git init --bare

# 在临时目录创建初始内容并推送到远程
TEMP=$(mktemp -d)
cd "$TEMP"
git init
git config user.name "Admin"
git config user.email "admin@example.com"
echo "# 团队项目" > README.md
echo "这是一个协作项目的初始版本" >> README.md
git add README.md
git commit -m "init: 项目初始化"

# 创建 develop 分支（团队开发主线）
git switch -c develop
echo "" >> README.md
echo "## 开发中..." >> README.md
git add README.md
git commit -m "chore: 初始化 develop 分支"

# 推送到远程（main 和 develop 两个分支）
git remote add origin "$REMOTE"
git push -u origin main
git push -u origin develop

rm -rf "$TEMP"


# ============================================================
# 1. Alice 克隆仓库，开发功能
# ============================================================
echo ""
echo ">>> [1] Alice：克隆仓库 → 开发登录功能"

git clone "$REMOTE" "$ALICE"
cd "$ALICE"
git config user.name "Alice"
git config user.email "alice@example.com"

# 切换到 develop 分支
git switch develop

# 创建功能分支（命名规范：feature/xxx）
git switch -c feature/alice-login

# Alice 开发登录功能
mkdir -p src
cat > src/login.py << 'PYEOF'
"""
登录模块
作者：Alice
"""
def login(username, password):
    """用户登录"""
    if not username or not password:
        return {"success": False, "message": "用户名和密码不能为空"}
    # TODO: 连接数据库验证
    if username == "admin" and password == "123456":
        return {"success": True, "message": "登录成功"}
    return {"success": False, "message": "用户名或密码错误"}


def validate_input(username, password):
    """输入验证"""
    if len(username) < 3:
        return False, "用户名至少 3 位"
    if len(password) < 6:
        return False, "密码至少 6 位"
    return True, "OK"
PYEOF

git add src/login.py
git commit -m "feat: 实现登录模块基本功能"

# Alice 再加一个功能
cat > src/session.py << 'PYEOF'
"""
会话管理
作者：Alice
"""
import uuid

sessions = {}

def create_session(user_id):
    """创建用户会话"""
    token = str(uuid.uuid4())
    sessions[token] = user_id
    return token

def validate_session(token):
    """验证会话是否有效"""
    return token in sessions

def destroy_session(token):
    """销毁会话"""
    sessions.pop(token, None)
PYEOF

git add src/session.py
git commit -m "feat: 添加会话管理模块"

echo ""
echo "Alice 的提交历史："
git log --oneline

# 推送功能分支到远程
git push -u origin feature/alice-login


# ============================================================
# 2. Bob 克隆仓库，开发功能
# ============================================================
echo ""
echo ">>> [2] Bob：克隆仓库 → 开发 API 模块"

git clone "$REMOTE" "$BOB"
cd "$BOB"
git config user.name "Bob"
git config user.email "bob@example.com"

# 切换到 develop
git switch develop

# 创建功能分支
git switch -c feature/bob-api

# Bob 开发 API 模块
mkdir -p src
cat > src/api.py << 'PYEOF'
"""
API 路由模块
作者：Bob
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    """健康检查"""
    return jsonify({"status": "ok", "version": "0.1.0"})

@app.route('/api/login', methods=['POST'])
def api_login():
    """登录接口"""
    data = request.get_json()
    # 调用 Alice 开发的 login 函数
    from src.login import login
    result = login(data.get('username'), data.get('password'))
    return jsonify(result)
PYEOF

git add src/api.py
git commit -m "feat: 创建 API 路由模块（/health + /api/login）"

# Bob 再添加配置
cat > config.py << 'PYEOF'
"""项目配置"""

DEBUG = True
SECRET_KEY = "dev-secret-key"  # 注意：生产环境要改！
DATABASE_URL = "sqlite:///app.db"
PORT = 5000
PYEOF

git add config.py
git commit -m "feat: 添加项目配置文件"

echo ""
echo "Bob 的提交历史："
git log --oneline

# 推送
git push -u origin feature/bob-api


# ============================================================
# 3. Alice 的 PR 先被审查 → 合并到 develop
# ============================================================
echo ""
echo ">>> [3] Code Review & Merge：Alice 的 PR 先通过审查"

cd "$ALICE"

# 模拟：Alice 收到 review 意见，需要修改
# "把硬编码的 admin/123456 改成从环境变量读取"
git switch feature/alice-login

cat > src/login.py << 'PYEOF'
"""
登录模块
作者：Alice
"""
import os

# 从环境变量读取默认管理员账号（不再硬编码）
DEFAULT_ADMIN = os.getenv("ADMIN_USERNAME", "admin")
DEFAULT_PASS = os.getenv("ADMIN_PASSWORD", "123456")


def login(username, password):
    """用户登录"""
    if not username or not password:
        return {"success": False, "message": "用户名和密码不能为空"}
    # TODO: 连接数据库验证
    if username == DEFAULT_ADMIN and password == DEFAULT_PASS:
        return {"success": True, "message": "登录成功"}
    return {"success": False, "message": "用户名或密码错误"}


def validate_input(username, password):
    """输入验证"""
    if len(username) < 3:
        return False, "用户名至少 3 位"
    if len(password) < 6:
        return False, "密码至少 6 位"
    return True, "OK"
PYEOF

git add src/login.py
git commit -m "fix: 管理员账号改为从环境变量读取（review 意见）"
git push

# 模拟合并 PR（在真实流程中是在 GitHub 网页上点 Merge）
# 这里手动操作：把 feature 合并到 develop
echo ""
echo "模拟 PR 合并：feature/alice-login → develop"
git switch develop
git merge feature/alice-login -m "Merge PR: feature/alice-login（Code Review 通过）"
git push origin develop

echo "Alice 的功能已合并到 develop！"


# ============================================================
# 4. Bob rebase 最新 develop → 解决可能的冲突
# ============================================================
echo ""
echo ">>> [4] Bob：rebase 到最新 develop（避免合并冲突）"

cd "$BOB"
git fetch origin

echo ""
echo "Bob 的 develop 和最新 origin/develop 的差异："
git log develop..origin/develop --oneline

# 更新本地 develop
git switch develop
git merge origin/develop   # develop 本地更新

# 把 Bob 的功能分支 rebase 到最新 develop 上
git switch feature/bob-api
echo ""
echo "执行 git rebase develop：把 Bob 的提交搬到最新 develop 上"
git rebase develop

echo ""
echo "rebase 成功！Bob 的历史现在是基于最新 develop 的"
git log --oneline --graph -10

# 推送（rebase 后需要 force-with-lease）
echo ""
echo "rebase 后推送：使用 --force-with-lease（比 --force 安全）"
echo "  --force-with-lease：如果远程有人推送了东西，会拒绝覆盖"
git push --force-with-lease origin feature/bob-api


# ============================================================
# 5. Bob 的 PR 合并 → develop → main
# ============================================================
echo ""
echo ">>> [5] 模拟 Bob 的 PR 合并：feature/bob-api → develop"

cd "$BOB"
git switch develop
git merge feature/bob-api -m "Merge PR: feature/bob-api（Code Review 通过）"
git push origin develop

echo "Bob 的功能也已合并到 develop！"


# ============================================================
# 6. 发布：develop → main（模拟 Release PR）
# ============================================================
echo ""
echo ">>> [6] 发布：develop → main"

cd "$ALICE"
git fetch origin
git switch develop
git pull origin develop

# 合并到 main
git switch main
git merge develop -m "release: v0.2.0 - 登录模块 + API 路由"

# 打版本标签
git tag -a "v0.2.0" -m "v0.2.0: 登录模块 + API 路由 + 会话管理"

# 推送 main 和标签
git push origin main
git push origin v0.2.0

echo "发布完成！v0.2.0 已推送到远程"


# ============================================================
# 7. 清理功能分支
# ============================================================
echo ""
echo ">>> [7] 清理已合并的功能分支"

cd "$ALICE"
git branch -d feature/alice-login 2>/dev/null || true
git push origin --delete feature/alice-login 2>/dev/null || true

cd "$BOB"
git branch -d feature/bob-api 2>/dev/null || true
git push origin --delete feature/bob-api 2>/dev/null || true

echo "功能分支已清理（本地和远程）"


# ============================================================
# 总结
# ============================================================
echo ""
echo "============================================"
echo "  团队协作模拟完成！"
echo ""
echo "  工作流回顾："
echo "  ┌─────────────────────────────────────────┐"
echo "  │ main ←──── develop ←── feature/alice-*  │"
echo "  │   ↑          ↑    └── feature/bob-*     │"
echo "  │  发布      开发主线    功能分支           │"
echo "  └─────────────────────────────────────────┘"
echo ""
echo "  今天练习的关键操作："
echo "  1. git switch -c feature/xxx  → 从 develop 创建功能分支"
echo "  2. 命名规范：feature/ fix/ hotfix/ refactor/ docs/"
echo "  3. Commit 规范：feat: fix: refactor: docs: test: chore:"
echo "  4. PR → Code Review → 修改 → 通过 → Merge"
echo "  5. git rebase develop         → 同步最新代码（直线历史）"
echo "  6. git push --force-with-lease → rebase 后安全推送"
echo "  7. git tag -a vX.Y.Z -m "..."  → 发布版本标签"
echo "  8. git branch -d + push --delete → 清理已合并分支"
echo ""
echo "  练习目录: $LABDIR（可以安全删除）"
echo "============================================"
