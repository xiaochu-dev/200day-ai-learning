"""
Day 12 参考答案 — 分治思想：二分查找 + 快速排序 + 归并排序 + LeetCode 704/912
========================================================================
完整可运行代码，做完练习后再对照参考。
"""


# ============================================================
# 第一部分：二分查找
# ============================================================

def binary_search(arr: list, target: int) -> int:
    """在有序数组 arr 中查找 target，返回索引；找不到返回 -1。"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # 防溢出写法
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # target 在右半边
        else:
            right = mid - 1  # target 在左半边

    return -1


def binary_search_recursive(arr: list, target: int,
                            left: int, right: int) -> int:
    """递归版二分查找。"""
    # 基线条件：搜索区间为空
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # 递归搜右半边
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        # 递归搜左半边
        return binary_search_recursive(arr, target, left, mid - 1)


# ============================================================
# 第二部分：快速排序
# ============================================================

def partition(arr: list, low: int, high: int) -> int:
    """选 arr[high] 为 pivot，小的放左，大的放右，返回 pivot 最终位置。"""
    pivot = arr[high]          # 选最后一个元素做基准
    i = low - 1                # i 指向"小于 pivot 的区域"的右边界

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 把小的换到左边

    # 把 pivot 放到正确位置（i+1）
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: list, low: int, high: int) -> None:
    """快速排序（原地排序）。"""
    if low < high:
        pi = partition(arr, low, high)  # pivot 已归位
        quick_sort(arr, low, pi - 1)    # 递归排左半边
        quick_sort(arr, pi + 1, high)   # 递归排右半边


# ============================================================
# 第三部分：归并排序
# ============================================================

def merge(left: list, right: list) -> list:
    """合并两个有序数组，返回新的有序数组。"""
    result = []
    i = j = 0

    # 双指针：每次取较小的元素
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 把剩余元素追加到末尾（最多只有一边还有剩余）
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr: list) -> list:
    """归并排序：返回排好序的新数组。"""
    # 基线条件：长度 ≤ 1，已经有序
    if len(arr) <= 1:
        return arr

    # 分：切成两半
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 治：递归排左右两边
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 合：合并两个有序数组
    return merge(left_sorted, right_sorted)


# ============================================================
# 第四部分：LeetCode 题目
# ============================================================

def search_704(nums: list, target: int) -> int:
    """LeetCode 704 — 二分查找"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def sort_array_912(nums: list) -> list:
    """LeetCode 912 — 排序数组（用归并排序实现）"""
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = sort_array_912(nums[:mid])
    right = sort_array_912(nums[mid:])

    # merge two sorted arrays
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ============================================================
# 测试代码
# ============================================================

if __name__ == "__main__":
    passed = 0
    total = 0

    # ---------- 二分查找 ----------
    print("=" * 50)
    print("二分查找测试")
    print("=" * 50)
    total += 4

    bs_arr = [1, 3, 5, 7, 9, 11, 13]
    if binary_search(bs_arr, 7) == 3:
        print("✅ binary_search 找到中间元素"); passed += 1
    else:
        print("❌ binary_search 找到中间元素")
    if binary_search(bs_arr, 6) == -1:
        print("✅ binary_search 找不到正确返回-1"); passed += 1
    else:
        print("❌ binary_search 找不到正确返回-1")
    if binary_search_recursive(bs_arr, 1, 0, len(bs_arr) - 1) == 0:
        print("✅ binary_search_recursive 找第一个"); passed += 1
    else:
        print("❌ binary_search_recursive 找第一个")
    if binary_search_recursive(bs_arr, 13, 0, len(bs_arr) - 1) == 6:
        print("✅ binary_search_recursive 找最后一个"); passed += 1
    else:
        print("❌ binary_search_recursive 找最后一个")

    # ---------- 快速排序 ----------
    print()
    print("=" * 50)
    print("快速排序测试")
    print("=" * 50)

    qs_cases = [
        ([5, 3, 8, 1, 9, 2], [1, 2, 3, 5, 8, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3], [3]),
        ([], []),
    ]
    total += len(qs_cases)
    for arr, expected in qs_cases:
        copy = arr[:]
        if len(copy) > 0:
            quick_sort(copy, 0, len(copy) - 1)
        label = str(arr) if len(arr) <= 6 else f"len={len(arr)}"
        if copy == expected:
            print(f"✅ 快排 {label}"); passed += 1
        else:
            print(f"❌ 快排 {label}: 得到 {copy}, 期望 {expected}")

    # ---------- 归并排序 ----------
    print()
    print("=" * 50)
    print("归并排序测试")
    print("=" * 50)

    total += len(qs_cases)
    for arr, expected in qs_cases:
        result = merge_sort(arr)
        label = str(arr) if len(arr) <= 6 else f"len={len(arr)}"
        if result == expected:
            print(f"✅ 归并 {label}"); passed += 1
        else:
            print(f"❌ 归并 {label}: 得到 {result}, 期望 {expected}")

    # ---------- LeetCode 704 ----------
    print()
    print("=" * 50)
    print("LeetCode 704 测试")
    print("=" * 50)
    total += 3
    if search_704([-1, 0, 3, 5, 9, 12], 9) == 4:
        print("✅ LC704 示例1"); passed += 1
    else:
        print("❌ LC704 示例1")
    if search_704([-1, 0, 3, 5, 9, 12], 2) == -1:
        print("✅ LC704 示例2"); passed += 1
    else:
        print("❌ LC704 示例2")
    if search_704([5], 5) == 0:
        print("✅ LC704 单元素"); passed += 1
    else:
        print("❌ LC704 单元素")

    # ---------- LeetCode 912 ----------
    print()
    print("=" * 50)
    print("LeetCode 912 测试")
    print("=" * 50)
    total += 2
    if sort_array_912([5, 2, 3, 1]) == [1, 2, 3, 5]:
        print("✅ LC912 示例1"); passed += 1
    else:
        print("❌ LC912 示例1")
    if sort_array_912([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]:
        print("✅ LC912 示例2"); passed += 1
    else:
        print("❌ LC912 示例2")

    # ---------- merge 函数单独测 ----------
    print()
    print("=" * 50)
    print("merge 函数测试")
    print("=" * 50)
    total += 3
    if merge([3, 5, 8], [1, 2, 9]) == [1, 2, 3, 5, 8, 9]:
        print("✅ merge 基本"); passed += 1
    else:
        print("❌ merge 基本")
    if merge([], [1, 2]) == [1, 2]:
        print("✅ merge 左空"); passed += 1
    else:
        print("❌ merge 左空")
    if merge([1, 2], []) == [1, 2]:
        print("✅ merge 右空"); passed += 1
    else:
        print("❌ merge 右空")

    print()
    print(f"通过: {passed}/{total}")
    if passed == total:
        print("🎉 全部通过！Day 12 完成！")
    else:
        print(f"还有 {total - passed} 个测试没通过，继续加油！")
