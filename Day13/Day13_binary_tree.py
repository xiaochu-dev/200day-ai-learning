"""
Day 13 — 二叉树基础：遍历（前/中/后序 + 层序）+ 二叉搜索树 + LeetCode 144/94/145/102
================================================================================
每个函数里留了 TODO 让你实现，跑通后去掉 TODO 注释。

参考答案在 Day13_binary_tree_答案.py，做完再对照。
"""

from collections import deque
from typing import Optional, List


# ============================================================
# 第零部分：TreeNode 定义
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
    """前序遍历：根 → 左 → 右（递归）。

    示例：
        1
       / \
      2   3
    返回 [1, 2, 3]
    """
    # TODO: 实现前序遍历
    def dfs(node, result):
        pass

    result = []
    dfs(root, result)
    return result


def inorder(root: Optional[TreeNode]) -> List[int]:
    """中序遍历：左 → 根 → 右（递归）。

    示例：
        2
       / \
      1   3
    返回 [1, 2, 3]（BST 中序遍历得到有序序列）
    """
    # TODO: 实现中序遍历
    def dfs(node, result):
        pass

    result = []
    dfs(root, result)
    return result


def postorder(root: Optional[TreeNode]) -> List[int]:
    """后序遍历：左 → 右 → 根（递归）。

    示例：
        1
       / \
      2   3
    返回 [2, 3, 1]
    """
    # TODO: 实现后序遍历
    def dfs(node, result):
        pass

    result = []
    dfs(root, result)
    return result


# ============================================================
# 第二部分：广度优先遍历（BFS）= 层序遍历
# ============================================================

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """层序遍历：返回二维列表，每个子列表是一层的节点值。

    示例：
        1
       / \
      2   3
     / \
    4   5
    返回 [[1], [2, 3], [4, 5]]

    提示：用 deque 做队列，for _ in range(len(queue)) 控制每层。
    """
    # TODO: 实现层序遍历
    pass


# ============================================================
# 第三部分：二叉搜索树（BST）
# ============================================================

def bst_search(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """在 BST 中查找 val，找到返回该节点，找不到返回 None。
    利用 BST 性质：左 < 根 < 右。

    >>> root = build_bst([8, 3, 10, 1, 6, 14, 4, 7])
    >>> bst_search(root, 6).val
    6
    >>> bst_search(root, 9) is None
    True
    """
    # TODO: 实现 BST 查找
    pass


def bst_insert(root: Optional[TreeNode], val: int) -> TreeNode:
    """在 BST 中插入 val，返回根节点。

    >>> root = None
    >>> root = bst_insert(root, 5)
    >>> root = bst_insert(root, 3)
    >>> root = bst_insert(root, 7)
    >>> inorder(root)  # 中序遍历验证有序
    [3, 5, 7]
    """
    # TODO: 实现 BST 插入
    pass


# ============================================================
# LeetCode 题目
# ============================================================

def preorder_144(root: Optional[TreeNode]) -> List[int]:
    """LeetCode 144 — 二叉树的前序遍历"""
    # TODO
    pass


def inorder_94(root: Optional[TreeNode]) -> List[int]:
    """LeetCode 94 — 二叉树的中序遍历"""
    # TODO
    pass


def postorder_145(root: Optional[TreeNode]) -> List[int]:
    """LeetCode 145 — 二叉树的后序遍历"""
    # TODO
    pass


def level_order_102(root: Optional[TreeNode]) -> List[List[int]]:
    """LeetCode 102 — 二叉树的层序遍历"""
    # TODO
    pass


# ============================================================
# 辅助函数（不用改）
# ============================================================

def build_bst(values: list) -> Optional[TreeNode]:
    """用列表构建一棵 BST，方便测试。"""
    root = None
    for v in values:
        root = bst_insert(root, v)
    return root


def build_tree_from_list(values: list) -> Optional[TreeNode]:
    """用层序列表构建二叉树（用于测试遍历）。
    None 表示空节点。例如 [1, 2, 3, None, None, 4, 5] 建树：
        1
       / \
      2   3
         / \
        4   5
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        # 左孩子
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # 右孩子
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ============================================================
# 测试代码（先别改这里，写完函数直接跑）
# ============================================================

if __name__ == "__main__":
    passed = 0
    total = 0

    # 构建测试树
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = build_tree_from_list([1, 2, 3, 4, 5, None, 6])

    # ---------- DFS 遍历 ----------
    print("=" * 50)
    print("DFS 遍历测试")
    print("=" * 50)
    total += 3

    if preorder(root) == [1, 2, 4, 5, 3, 6]:
        print("✅ 前序遍历"); passed += 1
    else:
        print(f"❌ 前序遍历: 得到 {preorder(root)}, 期望 [1, 2, 4, 5, 3, 6]")
    if inorder(root) == [4, 2, 5, 1, 3, 6]:
        print("✅ 中序遍历"); passed += 1
    else:
        print(f"❌ 中序遍历: 得到 {inorder(root)}, 期望 [4, 2, 5, 1, 3, 6]")
    if postorder(root) == [4, 5, 2, 6, 3, 1]:
        print("✅ 后序遍历"); passed += 1
    else:
        print(f"❌ 后序遍历: 得到 {postorder(root)}, 期望 [4, 5, 2, 6, 3, 1]")

    # ---------- 空树测试 ----------
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

    single = build_tree_from_list([1])
    if level_order(single) == [[1]]:
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
        print(f"❌ LC144")
    if inorder_94(lc_root) == [1, 3, 2]:
        print("✅ LC94 中序"); passed += 1
    else:
        print(f"❌ LC94")
    if postorder_145(lc_root) == [3, 2, 1]:
        print("✅ LC145 后序"); passed += 1
    else:
        print(f"❌ LC145")

    lc102_tree = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    if level_order_102(lc102_tree) == [[3], [9, 20], [15, 7]]:
        print("✅ LC102 层序"); passed += 1
    else:
        print(f"❌ LC102")

    print()
    print(f"通过: {passed}/{total}")
    if passed == total:
        print("🎉 全部通过！Day 13 完成！")
    else:
        print(f"还有 {total - passed} 个测试没通过，继续加油！")
