"""
Day8 — 手写单链表 + LeetCode 206 反转链表

⚠️ 每个 `# TODO:` 需要你补全。参考答案在末尾。
"""


# ============================================================
# TODO 1: Node 节点类
# ============================================================
class Node:
    """链表节点：存数据 + 指向下一个"""

    def __init__(self, data):
        # TODO: self.data = data, self.next = None
        self.data = data
        self.next = None


# ============================================================
# TODO 2: LinkedList 链表类
# ============================================================
class LinkedList:
    """单链表"""

    def __init__(self):
        # TODO: self.head = None
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        """
        尾部追加

        思路：
        - 如果链表为空（head is None），新节点就是 head
        - 否则从头走到尾，最后节点的 next 指向新节点
        """
        # TODO: 实现

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        """
        头部插入

        思路：
        - 新节点 .next = self.head
        - self.head = 新节点
        """
        # TODO: 实现

    def delete(self, data):
        if self.head is None:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return True
            curr = curr.next
        """
        删除第一个值为 data 的节点

        思路：
        - 特殊情况：head 就是要删的 → head = head.next
        - 一般情况：遍历，找到目标节点的前一个节点，跳过目标
        - 返回值：删掉了返回 True，没找到返回 False
        """
        # TODO: 实现


    def find(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False
        """
        查找，返回 True/False

        提示：从头走到尾，比较每个节点的 data
        """
        # TODO: 实现


    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

        """
        让链表可遍历：for node in linked_list

        提示：用 yield，从头走到尾
        """
        # TODO: 实现生成器


    def __str__(self):
        values = [str(node.data) for node in self]
        return ' -> '.join(values) + ' -> None'
        """
        打印链表：1 -> 2 -> 3 -> None

        提示：用列表推导式收集所有节点的 data，然后用 ' -> '.join()
        """
        # TODO: 实现



# ============================================================
# TODO 3: LeetCode 206 — 反转链表
# ============================================================
    def reverse(self):
        prev=None
        curr = self.head#1
        while curr:
            next_node = curr.next#2 3 4 5 None
            curr.next = prev#None 1 2 3 4
            prev = curr#1 2 3 4 5
            curr = next_node#2 3 4 5 None
        self.head = prev#5
        """
        原地反转链表

        输入: 1 → 2 → 3 → 4 → 5 → None
        输出: 5 → 4 → 3 → 2 → 1 → None

        经典三指针法：
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next   # 1. 保存下一个
            curr.next = prev        # 2. 当前指向前一个（反转！）
            prev = curr             # 3. prev 前进
            curr = next_node        # 4. curr 前进
        self.head = prev            # 最后 prev 就是新 head
        """
        # TODO: 实现三指针反转



# ============================================================
# 测试代码（写完取消注释测试）
# ============================================================
if __name__ == "__main__":
    pass
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print("链表:", ll)           # 0 -> 1 -> 2 -> 3 -> None
    print("查找2:", ll.find(2))  # True
    print("查找9:", ll.find(9))  # False
    ll.delete(2)
    print("删2后:", ll)          # 0 -> 1 -> 3 -> None
    ll.reverse()
    print("反转后:", ll)         # 3 -> 1 -> 0 -> None


# ============================================================
# 参考答案
# ============================================================
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False

    def find(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __str__(self):
        values = [str(node.data) for node in self]
        return ' -> '.join(values) + ' -> None'

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
"""
