# Day 8 — Week 3 开始：数组 & 链表

> **目标**：理解数组和链表的底层区别，手写单链表 + 1道LeetCode
> **时间**：约 90min Python + 30min 英语

---

## 一、核心概念（10min）

| | 数组 (Array/List) | 链表 (Linked List) |
|---|---|---|
| 内存 | 连续一块 | 散落各处，指针连接 |
| 访问 | O(1) — 直接下标 | O(n) — 从头遍历 |
| 插入/删除 | O(n) — 要挪位置 | O(1) — 改指针就行 |
| Python | `list` 内置 | 没有内置，要自己写 |

> **关键直觉**：数组像电影院连座（找人快，插人慢），链表像寻宝游戏（每个箱子告诉你下一个在哪）。

---

## 二、手写单链表（40min）

文件：`Day08_linked_list.py`

需要实现：

| 方法 | 功能 |
|------|------|
| `Node(data)` | 节点：存数据 + 指向下一个 |
| `LinkedList()` | 链表：维护 head 指针 |
| `append(data)` | 尾部追加 |
| `prepend(data)` | 头部插入 |
| `delete(data)` | 按值删除第一个匹配节点 |
| `find(data)` | 查找，返回 True/False |
| `__iter__()` + `__str__()` | 让链表可遍历、可打印 |

---

## 三、LeetCode 206 — 反转链表（25min）

**题目**：输入 `1→2→3→4→5→None`，输出 `5→4→3→2→1→None`

写到 `Day08_linked_list.py` 末尾，给 `LinkedList` 类加一个 `reverse()` 方法。

---

## 四、英语（30min）

- 单词：六级高频词 #211-240（见学习版 + 自测版）
- 听力：VOA 精听 1 篇

---

## 五、Git

```bash
cd E:\Users\MyFiles\Desktop\200day
git add .
git commit -m "Day8: 手写单链表 + LeetCode 206 反转链表"
git push
```

---

## 检查清单

- [ ] LinkedList 全部方法实现，能跑通
- [ ] reverse() 正确反转链表
- [ ] 理解数组 vs 链表的时间复杂度差异
- [ ] 单词自测填完
- [ ] VOA 听力完成
- [ ] commit + push
