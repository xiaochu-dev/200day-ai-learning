# Day 14 — 二叉树进阶：迭代遍历 + 树的性质判断

> Week 3 算法周 | 2026-07-31

---

## 今日目标

用**栈模拟递归**深入理解遍历原理，掌握三个经典树性质判断：最大深度、验证BST、平衡树。

---

## 一、迭代版中序遍历（栈模拟递归）

Day 13 用递归写遍历很简单，但递归底层就是**函数调用栈**。自己用栈模拟一遍，才算真正理解。

### 递归 vs 迭代

```
递归（隐式栈）：               迭代（显式栈）：
def inorder(root):            def inorder(root):
    if not root: return           stack = []
    inorder(root.left)            cur = root
    result.append(root.val)       while cur or stack:
    inorder(root.right)               ↓ 用手写的栈替代递归
```

### 迭代中序的套路

```
        1
       / \
      2   3
     / \
    4   5

步骤：
  一路向左压栈 → [1, 2, 4]
  弹 4，输出 4，cur = 4.right = None
  弹 2，输出 2，cur = 5
  一路向左压栈 → [1, 5]
  弹 5，输出 5，cur = None
  弹 1，输出 1，cur = 3
  一路向左压栈 → [3]
  弹 3，输出 3，cur = None
  栈空 → 结束

输出：4 → 2 → 5 → 1 → 3 ✅
```

### 通用模板

```python
stack = []
cur = root
while cur or stack:
    while cur:          # 一路向左走到头
        stack.append(cur)
        cur = cur.left
    cur = stack.pop()   # 弹出一个
    result.append(cur.val)
    cur = cur.right     # 转向右子树
```

### 任务
1. 实现 `inorder_iterative(root)` → 迭代版中序遍历（用栈）

---

## 二、二叉树的最大深度

### 核心思想

树的最大深度 = 从根到最远叶子的节点数。

```
        3              ← 深度 1
       / \
      9  20            ← 深度 2
         / \
        15  7          ← 深度 3  → 最大深度 = 3
```

**关键**：用 DFS 递归，父节点收集左右子树的结果。

```python
left = max_depth(root.left)    # 左子树深度
right = max_depth(root.right)  # 右子树深度
return max(left, right) + 1    # 取大的 + 自己这一层
```

### BFS 解法思路
层序遍历，每遍历一层 depth + 1，遍历完就是最大深度。

### 任务
2. 实现 `max_depth(root)` → 递归版（DFS）+ BFS 版两种写法

---

## 三、验证二叉搜索树（BST）

Day 13 学了 BST 的定义：**左 < 根 < 右**。但"小于根"不只是左孩子小就行，而是**左子树所有节点**都小于根。

### 陷阱：只看局部

```
        5
       / \
      1   8
         / \
        4   9    ← 4 < 8，但 4 < 5 ❌ 不在 5 的右子树范围！
```

根是 5，右子树所有节点必须 > 5。4 违反了。

### 正确做法：传递上下界

```python
def is_valid_bst(root, min_val=负无穷, max_val=正无穷):
    if not root: return True
    if root.val <= min_val or root.val >= max_val: return False  # 不在范围内
    return (is_valid_bst(root.left, min_val, root.val) and       # 左：上限收紧
            is_valid_bst(root.right, root.val, max_val))          # 右：下限收紧
```

还有一种做法：BST 的**中序遍历一定严格递增**。遍历一遍检查即可。

### 任务
3. 实现 `is_valid_bst(root)` → 两种方法都写（界限法 + 中序法）

---

## 四、平衡二叉树

### 定义

每个节点的 **|左深度 - 右深度| ≤ 1**，且左右子树自身也是平衡的。

```
      3              ← |1-2| = 1 ✅
     / \
    9  20            ← |0-1| = 1 ✅
       / \
      15  7          ← |0-0| = 0 ✅  → 整体平衡

      1
     / \
    2   3            ← |2-0| = 2 ❌
   / \
  4   5              → 不平衡！
```

### 思路

还是**自底向上**：先问左右子树平不平衡、深度多少，再判断自己。

```python
def check(root):
    if not root: return 0              # 空树深度 0
    left = check(root.left)
    right = check(root.right)
    if left == -1 or right == -1:      # 子树已不平衡，向上传 -1
        return -1
    if abs(left - right) > 1:          # 自己不平衡
        return -1
    return max(left, right) + 1        # 返回真实深度
```

### 任务
4. 实现 `is_balanced(root)` → 自底向上一次遍历

---

## 五、今日任务清单

### 代码练习
- [ ] `inorder_iterative` — 迭代版中序遍历（用栈模拟）
- [ ] `max_depth` — 最大深度（递归 DFS + BFS 两种）
- [ ] `is_valid_bst` — 验证 BST（界限法 + 中序法）
- [ ] `is_balanced` — 判断平衡二叉树

### LeetCode
- [ ] **#94 二叉树的中序遍历** — 用迭代法
- [ ] **#104 二叉树的最大深度**
- [ ] **#98 验证二叉搜索树**
- [ ] **#110 平衡二叉树**

### 英语
- [ ] 核心词 #126-150 自测（25词，过关线 20/25）
- [ ] VOA 精听 15 分钟

### 收尾
- [ ] 运行测试全部通过
- [ ] 提交代码：
  ```
  cd E:\Users\MyFiles\Desktop\200day
  git add Day14/
  git commit -m "Day14: 二叉树进阶——迭代遍历+最大深度+验证BST+平衡树 + LC94/98/104/110"
  git push
  ```

---

## 六、提示

1. **迭代遍历的 while 嵌套**：外层 `while cur or stack`，内层 `while cur` 一路向左
2. **验证 BST 别只看一层**——要传递 min/max 上下界，或者利用中序严格递增
3. **平衡树的 -1 标记**：用 -1 向上传"已不平衡"，避免重复计算深度
4. 代码模板在 `Day14_binary_tree_adv.py`，答案在 `Day14_binary_tree_adv_答案.py`（做完再看！）
5. 这些题是面试高频题，值得反复练
