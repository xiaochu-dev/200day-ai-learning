"""
Day 14 — 二叉树进阶 练习模板
================================
迭代遍历 + 最大深度 + 验证BST + 平衡树

每个函数只留 TODO，自己实现后再看答案文件。
"""

from collections import deque


class TreeNode:
    """二叉树节点（和 Day13 一样）"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 1. 迭代版中序遍历（用栈模拟递归）
# ============================================================

def inorder_iterative(root: TreeNode | None) -> list[int]:
    """用显式栈完成中序遍历（左→根→右），不使用递归"""
    # TODO: 实现迭代中序遍历

    pass


# ============================================================
# 2. 二叉树的最大深度
# ============================================================

def max_depth_dfs(root: TreeNode | None) -> int:
    """DFS 递归：最大深度 = max(左深度, 右深度) + 1"""
    # TODO: 递归计算最大深度

    pass


def max_depth_bfs(root: TreeNode | None) -> int:
    """BFS 层序遍历：每遍历一层 depth + 1"""
    # TODO: 层序遍历计算最大深度

    pass


# ============================================================
# 3. 验证二叉搜索树（BST）
# ============================================================

def is_valid_bst_bounds(root: TreeNode | None) -> bool:
    """界限法：递归传递 min/max 上下界"""
    # TODO: 用上下界验证 BST

    pass


def is_valid_bst_inorder(root: TreeNode | None) -> bool:
    """中序法：BST 的中序遍历必须严格递增"""
    # TODO: 用迭代中序遍历验证

    pass


# ============================================================
# 4. 判断平衡二叉树
# ============================================================

def is_balanced(root: TreeNode | None) -> bool:
    """每个节点 |左深度 - 右深度| ≤ 1"""
    # TODO: 自底向上一次遍历判断

    pass


# ============================================================
# 测试（写完代码后运行）
# ============================================================

if __name__ == "__main__":
    # 测试树一：正常树
    #        3
    #       / \
    #      9  20
    #         / \
    #        15  7
    t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    # 测试树二：非法 BST
    #        5
    #       / \
    #      1   8
    #         / \
    #        4   9
    t2 = TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(4), TreeNode(9)))

    # 测试树三：不平衡
    #        1
    #       /
    #      2
    #     /
    #    3
    t3 = TreeNode(1, TreeNode(2, TreeNode(3)), None)

    print("1. inorder_iterative:")
    print(f"   树 [3,9,20,null,null,15,7]: {inorder_iterative(t1)}")
    print("   期望: [9, 3, 15, 20, 7]")

    print("\n2. max_depth:")
    print(f"   DFS: {max_depth_dfs(t1)} (期望: 3)")
    print(f"   BFS: {max_depth_bfs(t1)} (期望: 3)")

    print("\n3. is_valid_bst:")
    print(f"   t1 界限法: {is_valid_bst_bounds(t1)} (期望: False, 9在3左边但>3)")
    print(f"   t1 中序法: {is_valid_bst_inorder(t1)} (期望: False)")
    print(f"   t2 界限法: {is_valid_bst_bounds(t2)} (期望: False, 4在5右子树但<5)")
    print(f"   t2 中序法: {is_valid_bst_inorder(t2)} (期望: False)")

    print("\n4. is_balanced:")
    print(f"   t1: {is_balanced(t1)} (期望: True)")
    print(f"   t3: {is_balanced(t3)} (期望: False)")

    print("\n✅ 全部通过? 检查上面的输出和期望是否一致")
