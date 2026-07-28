"""
Day 13 参考答案 — 二叉树基础：遍历 + 二叉搜索树 + LeetCode 144/94/145/102
========================================================================
完整可运行代码，做完练习后再对照参考。
"""

from collections import deque
from typing import Optional, List


# ============================================================
# TreeNode 定义
# ============================================================

class TreeNode:
    """二叉树节点。"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 第一部分：深度优先遍历（DFS）
# ============================================================

def preorder(root: Optional[TreeNode]) -> List[int]:
    """前序遍历：根 → 左 → 右"""
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)   # 根
        dfs(node.left)            # 左
        dfs(node.right)           # 右

    dfs(root)
    return result


def inorder(root: Optional[TreeNode]) -> List[int]:
    """中序遍历：左 → 根 → 右"""
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)            # 左
        result.append(node.val)   # 根
        dfs(node.right)           # 右

    dfs(root)
    return result


def postorder(root: Optional[TreeNode]) -> List[int]:
    """后序遍历：左 → 右 → 根"""
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)            # 左
        dfs(node.right)           # 右
        result.append(node.val)   # 根

    dfs(root)
    return result


# ============================================================
# 第二部分：广度优先遍历（BFS）= 层序遍历
# ============================================================

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """层序遍历：用队列，逐层收集。"""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        # 当前层的节点数 = 进入这层时队列的长度
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


# ============================================================
# 第三部分：二叉搜索树（BST）
# ============================================================

def bst_search(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """在 BST 中查找 val。利用左<根<右每次砍半。"""
    if not root:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return bst_search(root.left, val)   # 往左找
    else:
        return bst_search(root.right, val)  # 往右找


def bst_insert(root: Optional[TreeNode], val: int) -> TreeNode:
    """在 BST 中插入 val，返回根节点。"""
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)

    return root


# ============================================================
# LeetCode 题目
# ============================================================

def preorder_144(root: Optional[TreeNode]) -> List[int]:
    """LeetCode 144"""
    return preorder(root)


def inorder_94(root: Optional[TreeNode]) -> List[int]:
    """LeetCode 94"""
    return inorder(root)


def postorder_145(root: Optional[TreeNode]) -> List[int]:
    """LeetCode 145"""
    return postorder(root)


def level_order_102(root: Optional[TreeNode]) -> List[List[int]]:
    """LeetCode 102"""
    return level_order(root)


# ============================================================
# 辅助函数
# ============================================================

def build_bst(values: list) -> Optional[TreeNode]:
    """用列表构建一棵 BST，方便测试。"""
    root = None
    for v in values:
        root = bst_insert(root, v)
    return root


def build_tree_from_list(values: list) -> Optional[TreeNode]:
    """用层序列表构建二叉树（用于测试遍历）。"""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ============================================================
# 测试代码
# ============================================================

if __name__ == "__main__":
    passed = 0
    total = 0

    # 构建测试树
    root = build_tree_from_list([1, 2, 3, 4, 5, None, 6])

    # ---------- DFS 遍历 ----------
    print("=" * 50)
    print("DFS 遍历测试")
    print("=" * 50)
    total += 3
    if preorder(root) == [1, 2, 4, 5, 3, 6]:
        print("✅ 前序遍历"); passed += 1
    else:
        print(f"❌ 前序遍历: 得到 {preorder(root)}")
    if inorder(root) == [4, 2, 5, 1, 3, 6]:
        print("✅ 中序遍历"); passed += 1
    else:
        print(f"❌ 中序遍历: 得到 {inorder(root)}")
    if postorder(root) == [4, 5, 2, 6, 3, 1]:
        print("✅ 后序遍历"); passed += 1
    else:
        print(f"❌ 后序遍历: 得到 {postorder(root)}")

    # ---------- 空树 ----------
    total += 3
    if preorder(None) == []:
        print("✅ 前序空树"); passed += 1
    else:
        print("❌ 前序空树")
    if inorder(None) == []:
        print("✅ 中序空树"); passed += 1
    else:
        print("❌ 中序空树")
    if postorder(None) == []:
        print("✅ 后序空树"); passed += 1
    else:
        print("❌ 后序空树")

    # ---------- 层序遍历 ----------
    print()
    print("=" * 50)
    print("层序遍历测试")
    print("=" * 50)
    total += 3
    tree = build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    result = level_order(tree)
    expected = [[1], [2, 3], [4, 5, 6]]
    if result == expected:
        print("✅ 层序基本"); passed += 1
    else:
        print(f"❌ 层序基本: 得到 {result}, 期望 {expected}")
    if level_order(build_tree_from_list([1])) == [[1]]:
        print("✅ 层序单节点"); passed += 1
    else:
        print("❌ 层序单节点")
    if level_order(None) == []:
        print("✅ 层序空树"); passed += 1
    else:
        print("❌ 层序空树")

    # ---------- BST 查找 ----------
    print()
    print("=" * 50)
    print("BST 查找测试")
    print("=" * 50)
    bst = build_bst([8, 3, 10, 1, 6, 14, 4, 7])
    total += 3
    if bst_search(bst, 6) is not None and bst_search(bst, 6).val == 6:
        print("✅ BST 查找存在"); passed += 1
    else:
        print("❌ BST 查找存在")
    if bst_search(bst, 9) is None:
        print("✅ BST 查找不存在"); passed += 1
    else:
        print("❌ BST 查找不存在")
    if bst_search(None, 5) is None:
        print("✅ BST 查找空树"); passed += 1
    else:
        print("❌ BST 查找空树")

    # ---------- BST 插入 ----------
    print()
    print("=" * 50)
    print("BST 插入测试")
    print("=" * 50)
    bst2 = None
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst2 = bst_insert(bst2, v)
    total += 2
    if inorder(bst2) == [1, 3, 4, 5, 6, 7, 8]:
        print("✅ BST 插入后中序有序"); passed += 1
    else:
        print(f"❌ BST 插入后中序有序: 得到 {inorder(bst2)}")
    if preorder(bst2) == [5, 3, 1, 4, 7, 6, 8]:
        print("✅ BST 插入后结构正确"); passed += 1
    else:
        print(f"❌ BST 插入后结构正确: 得到 {preorder(bst2)}")

    # ---------- LeetCode ----------
    print()
    print("=" * 50)
    print("LeetCode 测试")
    print("=" * 50)
    lc_root = build_tree_from_list([1, None, 2, 3])
    total += 4
    if preorder_144(lc_root) == [1, 2, 3]:
        print("✅ LC144 前序"); passed += 1
    else:
        print("❌ LC144")
    if inorder_94(lc_root) == [1, 3, 2]:
        print("✅ LC94 中序"); passed += 1
    else:
        print("❌ LC94")
    if postorder_145(lc_root) == [3, 2, 1]:
        print("✅ LC145 后序"); passed += 1
    else:
        print("❌ LC145")

    lc102_tree = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    if level_order_102(lc102_tree) == [[3], [9, 20], [15, 7]]:
        print("✅ LC102 层序"); passed += 1
    else:
        print("❌ LC102")

    print()
    print(f"通过: {passed}/{total}")
    if passed == total:
        print("🎉 全部通过！Day 13 完成！")
    else:
        print(f"还有 {total - passed} 个测试没通过，继续加油！")
