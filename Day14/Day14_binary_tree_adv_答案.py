"""
Day 14 — 二叉树进阶 参考答案
================================
迭代遍历 + 最大深度 + 验证BST + 平衡树
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 1. 迭代版中序遍历
# ============================================================

def inorder_iterative(root: TreeNode | None) -> list[int]:
    result = []
    stack = []
    cur = root

    while cur or stack:
        # 一路向左走到头，沿途全部压栈
        while cur:
            stack.append(cur)
            cur = cur.left
        # 弹出一个，输出，然后转向右子树
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right

    return result


# ============================================================
# 2. 二叉树的最大深度
# ============================================================

def max_depth_dfs(root: TreeNode | None) -> int:
    if not root:
        return 0
    left = max_depth_dfs(root.left)
    right = max_depth_dfs(root.right)
    return max(left, right) + 1


def max_depth_bfs(root: TreeNode | None) -> int:
    if not root:
        return 0
    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):  # 处理当前层所有节点
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


# ============================================================
# 3. 验证二叉搜索树（BST）
# ============================================================

def is_valid_bst_bounds(root: TreeNode | None) -> bool:
    def validate(node: TreeNode | None, low: float, high: float) -> bool:
        if not node:
            return True
        # 不在开区间 (low, high) 内 → 非法
        if node.val <= low or node.val >= high:
            return False
        # 左子树：上限收紧为当前值；右子树：下限收紧为当前值
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root, float("-inf"), float("inf"))


def is_valid_bst_inorder(root: TreeNode | None) -> bool:
    """BST 的中序遍历结果必须严格递增"""
    stack = []
    cur = root
    prev = float("-inf")

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        # 当前值必须 > 前一个值（严格递增）
        if cur.val <= prev:
            return False
        prev = cur.val
        cur = cur.right

    return True


# ============================================================
# 4. 判断平衡二叉树
# ============================================================

def is_balanced(root: TreeNode | None) -> bool:
    def check(node: TreeNode | None) -> int:
        """返回树的高度，不平衡时返回 -1"""
        if not node:
            return 0

        left = check(node.left)
        if left == -1:           # 左子树已不平衡
            return -1

        right = check(node.right)
        if right == -1:          # 右子树已不平衡
            return -1

        if abs(left - right) > 1:  # 自己不平衡
            return -1

        return max(left, right) + 1  # 返回真实高度

    return check(root) != -1


# ============================================================
# LeetCode 提交版本
# ============================================================

# LC #94 迭代中序（和上面一样，独立给 LeetCode 粘贴用）
def inorderTraversal(root: TreeNode | None) -> list[int]:
    result = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    return result


# LC #104 最大深度
def maxDepth(root: TreeNode | None) -> int:
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


# LC #98 验证BST
def isValidBST(root: TreeNode | None) -> bool:
    def validate(node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root, float("-inf"), float("inf"))


# LC #110 平衡树
def isBalanced(root: TreeNode | None) -> bool:
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return check(root) != -1


# ============================================================
# 测试
# ============================================================

if __name__ == "__main__":
    # 树一：正常树（非BST，用于遍历和深度测试）
    #        3
    #       / \
    #      9  20
    #         / \
    #        15  7
    t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    # 树二：合法 BST
    #        8
    #       / \
    #      3   10
    #     / \    \
    #    1   6    14
    #       / \
    #      4   7
    t2 = TreeNode(8,
            TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
            TreeNode(10, None, TreeNode(14)))

    # 树三：非法 BST（4 在 5 的右子树但小于 5）
    t3 = TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(4), TreeNode(9)))

    # 树四：不平衡（左子树深度远大于右子树）
    #        1
    #       /
    #      2
    #     /
    #    3
    t4 = TreeNode(1, TreeNode(2, TreeNode(3)), None)

    passed = 0
    total = 12

    # 1. 迭代中序
    r1 = inorder_iterative(t1)
    assert r1 == [9, 3, 15, 20, 7], f"期望 [9,3,15,20,7]，得到 {r1}"
    print(f"✅ 1. inorder_iterative: {r1}"); passed += 1

    # 2. 最大深度
    assert max_depth_dfs(t1) == 3, f"DFS 期望 3，得到 {max_depth_dfs(t1)}"
    print("✅ 2. max_depth_dfs 通过"); passed += 1

    assert max_depth_bfs(t1) == 3, f"BFS 期望 3，得到 {max_depth_bfs(t1)}"
    print("✅ 3. max_depth_bfs 通过"); passed += 1

    assert max_depth_dfs(None) == 0; print("✅ 4. 空树深度=0 通过"); passed += 1
    assert max_depth_dfs(TreeNode(1)) == 1; print("✅ 5. 单节点深度=1 通过"); passed += 1

    # 3. 验证 BST（t2 是合法BST，t3 是非法BST）
    assert is_valid_bst_bounds(t2) == True; print("✅ 6. BST界限法 t2(合法) 通过"); passed += 1
    assert is_valid_bst_bounds(t3) == False; print("✅ 7. BST界限法 t3(非法) 通过"); passed += 1
    assert is_valid_bst_inorder(t2) == True; print("✅ 8. BST中序法 t2(合法) 通过"); passed += 1
    assert is_valid_bst_inorder(t3) == False; print("✅ 9. BST中序法 t3(非法) 通过"); passed += 1

    # 4. 平衡（t1 平衡，t4 不平衡）
    assert is_balanced(t1) == True; print("✅ 10. is_balanced t1(平衡) 通过"); passed += 1
    assert is_balanced(t4) == False; print("✅ 11. is_balanced t4(不平衡) 通过"); passed += 1
    assert is_balanced(None) == True; print("✅ 12. 空树平衡 通过"); passed += 1

    print(f"\n🎉 {passed}/{total} 全部通过！")
