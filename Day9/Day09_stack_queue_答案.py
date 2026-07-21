"""Day 9 — 栈 & 队列 + LeetCode 20 有效括号"""


# ============================================================
# 一、Stack 类（用 list 实现，LIFO）
# ============================================================
class Stack:
    """栈：后进先出（LIFO），用 list 尾部模拟栈顶"""

    def __init__(self):
        self._items = []

    def push(self, item):
        """压入栈顶"""
        self._items.append(item)

    def pop(self):
        """弹出栈顶，空栈抛异常"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """看栈顶，不弹出"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """是否为空"""
        return len(self._items) == 0

    def size(self) -> int:
        """栈内元素个数"""
        return len(self._items)

    def __str__(self):
        return f"Stack(bottom->top): {self._items}"


# ============================================================
# 二、Queue 类（用 list 实现，FIFO）
# ============================================================
class Queue:
    """
    队列：先进先出（FIFO），用 list 实现。
    注意：dequeue 用 pop(0) 是 O(n)，生产环境应使用 collections.deque。
    """

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """入队（加到队尾）"""
        self._items.append(item)

    def dequeue(self):
        """出队（从队头取），空队抛异常"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self):
        """看队头，不取出"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """是否为空"""
        return len(self._items) == 0

    def size(self) -> int:
        """队列元素个数"""
        return len(self._items)

    def __str__(self):
        return f"Queue(front->rear): {self._items}"


# ============================================================
# 三、LeetCode 20 — 有效的括号
# ============================================================
def is_valid(s: str) -> bool:
    """
    判断括号字符串是否合法配对。
    使用栈：遇左括号 push，遇右括号 pop 检查是否匹配。

    >>> is_valid("()[]{}")
    True
    >>> is_valid("([)]")
    False
    >>> is_valid("{[]}")
    True
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in "([{":             # 左括号 → 入栈
            stack.append(ch)
        elif ch in ")]}":           # 右括号 → 出栈匹配
            if not stack:           # 栈空 = 多了右括号
                return False
            if stack.pop() != pairs[ch]:
                return False        # 类型不匹配
        # 其他字符忽略

    return len(stack) == 0          # 栈空 = 全部配对完毕


# ============================================================
# 测试
# ============================================================
if __name__ == "__main__":
    # --- Stack 测试 ---
    print("=== Stack Test ===")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)                        # Stack(bottom→top): [1, 2, 3]
    print("peek:", s.peek())        # 3
    print("pop:", s.pop())          # 3
    print("size:", s.size())        # 2
    print("is_empty:", s.is_empty()) # False
    print(s.pop())                  # 2
    print(s.pop())                  # 1
    print("is_empty:", s.is_empty()) # True
    try:
        s.pop()
    except IndexError as e:
        print("空栈pop异常:", e)

    # --- Queue 测试 ---
    print("\n=== Queue Test ===")
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q)                        # Queue(front→rear): ['a', 'b', 'c']
    print("peek:", q.peek())        # a
    print("dequeue:", q.dequeue())  # a
    print("dequeue:", q.dequeue())  # b
    print("size:", q.size())        # 1
    print(q.dequeue())              # c
    print("is_empty:", q.is_empty()) # True
    try:
        q.dequeue()
    except IndexError as e:
        print("空队dequeue异常:", e)

    # --- LeetCode 20 测试 ---
    print("\n=== Valid Parentheses Test ===")
    test_cases = [
        ("()[]{}", True),
        ("([)]", False),
        ("{[]}", True),
        ("(", False),
        ("", True),
        ("((", False),
        ("))", False),
        ("[(])", False),
    ]
    for expr, expected in test_cases:
        result = is_valid(expr)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] is_valid({expr!r}) = {result} (expected {expected})")

    print("\nDay09 完成！")
