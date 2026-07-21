"""Day 9 — 栈 & 队列 + LeetCode 20 有效括号"""


# ============================================================
# 一、Stack 类（用 list 实现，LIFO）
# ============================================================
class Stack:
    """栈：后进先出（LIFO），用 list 尾部模拟栈顶"""

    def __init__(self):
        # TODO: 初始化一个空列表
        self._items = []

    def push(self, item):
        """压入栈顶"""
        # TODO: 把 item 加到列表末尾
        self._items.append(item)

    def pop(self):
        """弹出栈顶，空栈抛异常"""
        # TODO: 如果栈空，raise IndexError("pop from empty stack")
        # TODO: 返回并删除列表最后一个元素
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """看栈顶，不弹出"""
        # TODO: 如果栈空，raise IndexError("peek from empty stack")
        # TODO: 返回列表最后一个元素（不删除）
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """是否为空"""
        # TODO: 判断列表长度是否为 0
        return len(self._items) == 0

    def size(self) -> int:
        """栈内元素个数"""
        # TODO: 返回列表长度
        return len(self._items)

    def __str__(self):
        # TODO: 返回 f"Stack(bottom->top): {列表内容}"
        return f"Stack(bottom->top): {self._items}"


# ============================================================
# 二、Queue 类（用 list 实现，FIFO）
# ============================================================
class Queue:
    """队列：先进先出（FIFO），用 list 实现"""

    def __init__(self):
        # TODO: 初始化一个空列表
        self._items = []

    def enqueue(self, item):
        """入队（加到队尾）"""
        # TODO: 把 item 加到列表末尾
        self._items.append(item)

    def dequeue(self):
        """出队（从队头取），空队抛异常"""
        # TODO: 如果队空，raise IndexError("dequeue from empty queue")
        # TODO: 返回并删除列表第一个元素
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self):
        """看队头，不取出"""
        # TODO: 如果队空，raise IndexError("peek from empty queue")
        # TODO: 返回列表第一个元素（不删除）
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """是否为空"""
        # TODO: 判断列表长度是否为 0
        return len(self._items) == 0

    def size(self) -> int:
        """队列元素个数"""
        # TODO: 返回列表长度
        return len(self._items)

    def __str__(self):
        # TODO: 返回 f"Queue(front->rear): {列表内容}"
        return f"Queue(bottom->top): {self._items}"


# ============================================================
# 三、LeetCode 20 — 有效的括号
# ============================================================
def is_valid(s: str) -> bool:
    """
    判断括号字符串是否合法配对。
    思路：遇左括号入栈，遇右括号出栈检查是否匹配。

    例：is_valid("()[]{}") → True
        is_valid("([)]") → False
        is_valid("{[]}") → True
    """
    # TODO: 创建配对字典 pairs = {")": "(", "]": "[", "}": "{"}
    # TODO: 创建空列表 stack
    # TODO: 遍历 s 中每个字符 ch：
    #   - 如果 ch 是左括号 "([{" → stack.append(ch)
    #   - 如果 ch 是右括号 ")]}" →
    #       - 如果 stack 为空 → return False（多了右括号）
    #       - 如果 stack.pop() != pairs[ch] → return False（类型不匹配）
    # TODO: 最后 return len(stack) == 0（栈空=全部配对）
    pairs = {")","(","]","[","}","{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack:
                return False
            if stack.pop()!=pairs[ch]:
                return False
    return len(stack) == 0


# ============================================================
# 测试（不要改这部分）
# ============================================================
if __name__ == "__main__":
    # --- Stack 测试 ---
    print("=== Stack Test ===")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)                        # Stack(bottom->top): [1, 2, 3]
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
        print("empty stack pop error:", e)

    # --- Queue 测试 ---
    print("\n=== Queue Test ===")
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q)                        # Queue(front->rear): ['a', 'b', 'c']
    print("peek:", q.peek())        # a
    print("dequeue:", q.dequeue())  # a
    print("dequeue:", q.dequeue())  # b
    print("size:", q.size())        # 1
    print(q.dequeue())              # c
    print("is_empty:", q.is_empty()) # True
    try:
        q.dequeue()
    except IndexError as e:
        print("empty queue dequeue error:", e)

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

    print("\nDay09 done!")
