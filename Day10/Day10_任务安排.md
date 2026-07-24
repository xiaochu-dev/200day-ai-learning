# Day 10 — 哈希表 & 字典

> **目标**：理解哈希表的底层原理，手写简易 HashMap + 1道LeetCode
> **时间**：约 90min Python + 30min 英语

---

## 一、核心概念（10min）

| | 数组 (Array) | 链表 (Linked List) | 哈希表 (Hash Table) |
|---|---|---|---|
| 访问 | O(1) — 下标直达 | O(n) — 从头找 | **O(1) — key 直达（平均）** |
| 插入 | O(n) — 挪位置 | O(1) — 改指针 | **O(1) — 平均** |
| 删除 | O(n) | O(1) | **O(1) — 平均** |
| 本质 | 整数索引 → 值 | 节点指针链 | **任意 key → hash code → 值** |

> **关键直觉**：哈希表 = 数组 + 哈希函数。把任意 key 算出一个整数，当数组下标用。这就是为什么 dict 取数据是 O(1)。Python 的 `dict` 和 `set` 底层都是哈希表。

### 哈希碰撞怎么办？

两个不同 key 算出同一个下标 → **链地址法**：每个桶里存一个链表，碰撞了就追加到链表上。

---

## 二、手写简易 HashMap（40min）

文件：`Day10_hash_table.py`

用**数组 + 链表（链地址法）**实现一个 HashMap：

| 方法 | 功能 |
|------|------|
| `HashMap(size=10)` | 初始化桶数组 |
| `_hash(key)` | 哈希函数：`sum(ord(c) for c in str(key)) % size` |
| `put(key, value)` | 存入键值对（key 已存在则更新） |
| `get(key)` | 取值，key 不存在返回 None |
| `remove(key)` | 删除键值对 |
| `contains(key)` | 判断 key 是否存在，返回 True/False |
| `keys()` | 返回所有 key 的列表 |
| `__str__()` | 打印整个哈希表结构 |

> **提示**：每个桶是一个列表 `[(key, value), ...]`，碰撞时 append，查找时遍历桶内列表。

---

## 三、LeetCode 1 — 两数之和（25min）

**题目**：给定数组和目标值，找出和为 target 的两个数的下标。
- `nums = [2, 7, 11, 15], target = 9` → 返回 `[0, 1]`（2+7=9）
- 假设只有一组答案，同一个元素不能用两次。

**思路**：遍历数组，用 dict 记录 `{值: 下标}`。每到一个数，查 `target - 当前数` 是否在 dict 里。

写到 `Day10_hash_table.py` 末尾，实现 `two_sum(nums, target)` 函数。

---

## 四、英语（30min）

- **单词（15min）**：核心词 #26-50，见 `Day10_单词学习.txt`
- **听力（15min）**：VOA 常速 1 篇，精听（听不懂倒回去，直到每句都听清）

---

## 五、Git

```bash
cd E:\Users\MyFiles\Desktop\200day
git add .
git commit -m "Day10: 手写HashMap + LeetCode 1 两数之和"
git push
```

---

## 检查清单

- [ ] HashMap 全部 7 个方法实现，能跑通
- [ ] LeetCode 1 两数之和 O(n) 解法
- [ ] 理解为什么 dict 查询是 O(1)
- [ ] 单词自测 >= 18/25
- [ ] VOA 听力 1 篇精听
- [ ] commit + push
