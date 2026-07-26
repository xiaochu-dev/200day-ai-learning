# Day 11 — 递归基础 + 排序算法（冒泡/选择/插入）

> **目标**：掌握递归思维，手写三种基础排序 + 1道LeetCode
> **时间**：约 90min Python + 30min 英语

---

## 一、递归基础（15min）

### 什么是递归？

函数自己调用自己。两个要素缺一不可：

| 要素 | 含义 | 例子（阶乘） |
|------|------|-------------|
| **基线条件** (base case) | 什么时候停下来 | `n == 1` 时返回 1 |
| **递归条件** (recursive case) | 怎么缩小问题 | `n * factorial(n-1)` |

```python
def factorial(n):
    if n == 1:          # 基线条件
        return 1
    return n * factorial(n - 1)   # 递归条件

print(factorial(5))  # 120
```

### 调用栈（Call Stack）

```
factorial(3)  → 压栈
  factorial(2)  → 压栈
    factorial(1)  → 压栈，命中基线，返回1
  factorial(2)  → 收到 1，返回 2*1=2，弹栈
factorial(3)  → 收到 2，返回 3*2=6，弹栈
```

> **关键直觉**：递归 = 把大问题拆成相同结构的小问题，直到小到可以直接解决。

### 递归经典练习（写到 `Day11_sorting.py` 里）

| 函数 | 要求 |
|------|------|
| `fib(n)` | 返回第 n 个斐波那契数（n≥1），递归实现 |
| `sum_list(arr)` | 递归求数组元素之和（不用 `sum()` 也不用循环） |
| `reverse_string(s)` | 递归反转字符串 |

---

## 二、冒泡排序 Bubble Sort（15min）

**思想**：每一轮把最大的元素"冒"到最右边。相邻两两比较，大的往后换。

```
第1轮：[5, 3, 8, 1] → [3, 5, 1, 8]   ← 8 归位
第2轮：[3, 5, 1, 8] → [3, 1, 5, 8]   ← 5 归位
第3轮：[3, 1, 5, 8] → [1, 3, 5, 8]   ← 3 归位，排序完成
```

**复杂度**：
- 时间：O(n²) 最坏/平均，O(n) 最好（已有序 + 提前结束优化）
- 空间：O(1) 原地排序

**优化**：如果某一轮没有发生交换，说明已经排好了，直接结束。

---

## 三、选择排序 Selection Sort（15min）

**思想**：每一轮找到未排序部分的最小值，放到已排序部分的末尾。

```
第1轮：[5, 3, 8, 1] → 找最小(1) → [1, 5, 3, 8]   ← 1 归位
第2轮：[1, 5, 3, 8] → 找最小(3) → [1, 3, 5, 8]   ← 3 归位
第3轮：[1, 3, 5, 8] → 找最小(5) → [1, 3, 5, 8]   ← 5 归位
```

**复杂度**：
- 时间：O(n²) 无论什么情况
- 空间：O(1) 原地排序

> **与冒泡的区别**：冒泡每轮交换很多次，选择排序每轮只交换一次（把最小值换到前面）。

---

## 四、插入排序 Insertion Sort（15min）

**思想**：像打扑克牌理牌——每次拿一张新牌，插入到已排序部分的正确位置。

```
第1步：[5 | 3, 8, 1] → 拿3，插到5前面 → [3, 5 | 8, 1]
第2步：[3, 5 | 8, 1] → 拿8，比5大放后面 → [3, 5, 8 | 1]
第3步：[3, 5, 8 | 1] → 拿1，逐个往前比 → [1, 3, 5, 8]
```

**复杂度**：
- 时间：O(n²) 最坏/平均，O(n) 最好（已有序）
- 空间：O(1) 原地排序

> **实际价值**：对小规模数据（n<50）或"基本有序"的数据，插入排序比快排还快。Python 的 `list.sort()`（Timsort）就内置了插入排序来处理小片段。

---

## 五、三种排序对比

| | 冒泡 | 选择 | 插入 |
|---|---|---|---|
| 最好 | O(n) | O(n²) | O(n) |
| 平均 | O(n²) | O(n²) | O(n²) |
| 最坏 | O(n²) | O(n²) | O(n²) |
| 空间 | O(1) | O(1) | O(1) |
| 稳定 | ✅ | ❌ | ✅ |
| 交换次数 | 多 | 少（每轮1次） | 视情况 |

> 稳定 = 相等元素排序后相对顺序不变。比如按成绩排序，同分的保持原顺序。

---

## 六、LeetCode 88 — 合并两个有序数组（15min）

**题目**：两个非递减数组 `nums1` 和 `nums2`，将 `nums2` 合并到 `nums1` 中，使 `nums1` 有序。

- `nums1 = [1,2,3,0,0,0], m = 3`（前3个有效，后面是占位0）
- `nums2 = [2,5,6], n = 3`
- 结果：`nums1 = [1,2,2,3,5,6]`

**要求**：原地修改 `nums1`，不要返回新数组。

**思路——三指针从后往前**：

```
nums1 = [1, 2, 3, 0, 0, 0]   nums2 = [2, 5, 6]
              ↑p1     ↑tail               ↑p2

从后往前填充：tail 指向 nums1 末尾，p1 指向 nums1 有效元素末尾，p2 指向 nums2 末尾。
每一步比较 nums1[p1] 和 nums2[p2]，大的放到 tail 位置，对应指针前移。

为什么从后往前？因为从前往后会覆盖还没处理的元素。从后往前利用了 nums1 末尾的空白空间。
```

写到 `Day11_sorting.py` 末尾，实现 `merge(nums1, m, nums2, n)` 函数。

---

## 七、英语（30min）

- **单词（15min）**：核心词 #51-75，见 `Day11_单词学习.txt`
- **听力（15min）**：VOA 常速 1 篇，精听（听不懂倒回去，直到每句都听清）

---

## 八、Git

```bash
cd E:\Users\MyFiles\Desktop\200day
git add .
git commit -m "Day11: 递归+冒泡/选择/插入排序 + LeetCode 88 合并有序数组"
git push
```

---

## 检查清单

- [ ] 递归 3 个函数能跑通（fib / sum_list / reverse_string）
- [ ] 冒泡排序实现（含提前结束优化）
- [ ] 选择排序实现
- [ ] 插入排序实现
- [ ] LeetCode 88 合并有序数组（原地、O(m+n)）
- [ ] 三种排序复杂度理解，能手写
- [ ] 单词自测 >= 20/25
- [ ] VOA 听力 1 篇精听
- [ ] commit + push

---

## 参考答案（做完再看 ↓↓↓）

<details>
<summary>点击展开参考答案</summary>

### 递归

```python
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def sum_list(arr):
    if not arr:          # 空数组 = 0
        return 0
    return arr[0] + sum_list(arr[1:])


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
```

### 冒泡排序

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:    # 本轮没交换，已有序
            break
    return arr
```

### 选择排序

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### 插入排序

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### LeetCode 88

```python
def merge(nums1, m, nums2, n):
    p1, p2 = m - 1, n - 1
    tail = m + n - 1

    while p2 >= 0:   # 只要 nums2 还有元素要放
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[tail] = nums1[p1]
            p1 -= 1
        else:
            nums1[tail] = nums2[p2]
            p2 -= 1
        tail -= 1
```

</details>
