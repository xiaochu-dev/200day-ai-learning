"""
Day 11 — 递归基础 + 排序算法（冒泡/选择/插入）+ LeetCode 88
==============================================================
每个函数里留了 TODO 让你实现，跑通后去掉 TODO 注释。

参考答案在 Day11_任务安排.md 底部，做完再对照。
"""

# ============================================================
# 第一部分：递归基础
# ============================================================

def fib(n: int) -> int:
    """递归求第 n 个斐波那契数（n ≥ 1）。
    fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3, fib(5) = 5
    """
    # TODO: 实现递归版本
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)


def sum_list(arr: list) -> int:
    """递归求数组元素之和（不用 sum() 也不用 for/while）。
    sum_list([1, 2, 3]) → 6
    sum_list([]) → 0
    """
    # TODO: 实现递归版本
    if not arr:
        return 0
    return arr[0] + sum_list(arr[1:])


def reverse_string(s: str) -> str:
    """递归反转字符串。
    reverse_string("abc") → "cba"
    reverse_string("") → ""
    """
    # TODO: 实现递归版本
    if len(s)<=1:
        return s
    return reverse_string(s[1:])+s[0]


# ============================================================
# 第二部分：三种排序
# ============================================================

def bubble_sort(arr: list) -> list:
    """冒泡排序：每一轮把最大值冒到最右边。
    优化：如果一轮没发生交换，提前结束。
    """
    # TODO: 实现冒泡排序
    n=len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr: list) -> list:
    """选择排序：每一轮找到未排序部分的最小值，放到已排序末尾。
    """
    # TODO: 实现选择排序
    n=len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr: list) -> list:
    """插入排序：像理扑克牌，每次拿一张插到正确位置。
    """
    # TODO: 实现插入排序
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


# ============================================================
# 第三部分：LeetCode 88 — 合并两个有序数组
# ============================================================

def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    """原地合并 nums2 到 nums1，结果保持有序。
    nums1 前 m 个是有效元素，后面 n 个是占位 0。

    示例：
    >>> nums1 = [1, 2, 3, 0, 0, 0]
    >>> merge(nums1, 3, [2, 5, 6], 3)
    >>> nums1
    [1, 2, 2, 3, 5, 6]

    提示：从后往前填，三指针（p1, p2, tail）。
    """
    # TODO: 实现 merge
    p1 ,p2=m-1, n-1
    tail = m+n-1
    while p2>0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[tail] = nums2[p1]
            p1-=1
        else:
            nums1[tail] = nums2[p2]
            p2-=1
        tail-=1


# ============================================================
# 测试代码（先别改这里，写完函数直接跑）
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("递归测试")
    print("=" * 50)
    print(f"fib(5) = {fib(5)}           # 预期: 5")
    print(f"fib(7) = {fib(7)}           # 预期: 13")
    print(f"sum_list([1,2,3,4,5]) = {sum_list([1, 2, 3, 4, 5])}  # 预期: 15")
    print(f'sum_list([]) = {sum_list([])}             # 预期: 0')
    print(f"reverse_string('hello') = {reverse_string('hello')}   # 预期: 'olleh'")
    print(f"reverse_string('') = {reverse_string('')}        # 预期: ''")

    print()
    print("=" * 50)
    print("排序测试")
    print("=" * 50)

    test_cases = [
        [5, 3, 8, 1, 9, 2],
        [1, 2, 3, 4, 5],      # 已有序
        [5, 4, 3, 2, 1],      # 逆序
        [3],
        [],
    ]

    for arr in test_cases:
        print(f"原数组: {arr}")
        print(f"  冒泡: {bubble_sort(arr[:])}")
        print(f"  选择: {selection_sort(arr[:])}")
        print(f"  插入: {insertion_sort(arr[:])}")
        print()

    print("=" * 50)
    print("LeetCode 88 测试")
    print("=" * 50)

    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    print(f"测试1: nums1 = {nums1}   # 预期: [1, 2, 2, 3, 5, 6]")

    nums1 = [0]
    merge(nums1, 0, [1], 1)
    print(f"测试2: nums1 = {nums1}          # 预期: [1]")

    nums1 = [1]
    merge(nums1, 1, [], 0)
    print(f"测试3: nums1 = {nums1}          # 预期: [1]")

    print()
    print("全部跑通 = Day 11 完成 ✅")
