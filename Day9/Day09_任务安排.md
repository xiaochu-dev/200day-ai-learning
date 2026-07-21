# Day 9 — 栈 & 队列

> **目标**：理解栈和队列的底层逻辑，手写实现 + 1道LeetCode
> **时间**：约 90min Python + 30min 英语

---

## 一、核心概念（10min）

| | 栈 (Stack) | 队列 (Queue) |
|---|---|---|
| 规则 | LIFO — 后进先出 | FIFO — 先进先出 |
| 比喻 | 一摞盘子，最后放的最先拿 | 排队买饭，先来的先打 |
| 操作 | push(压入) / pop(弹出) / peek(看顶部) | enqueue(入队) / dequeue(出队) |
| Python | `list` 模拟（append + pop） | `collections.deque`（双端队列） |

> **关键直觉**：栈是"撤销操作"的底层（Ctrl+Z），队列是"消息排队"的底层。

---

## 二、手写栈和队列（30min）

文件：`Day09_stack_queue.py`

需要实现：

### Stack 类（用 list 实现）
| 方法 | 功能 |
|------|------|
| `push(item)` | 压入栈顶 |
| `pop()` | 弹出栈顶，空栈抛异常 |
| `peek()` | 看栈顶，不弹出 |
| `is_empty()` | 是否为空 |
| `size()` | 栈内元素个数 |
| `__str__()` | 打印栈内容 |

### Queue 类（用 list 实现，不用 deque）
| 方法 | 功能 |
|------|------|
| `enqueue(item)` | 入队（加到队尾） |
| `dequeue()` | 出队（从队头取），空队抛异常 |
| `peek()` | 看队头，不取出 |
| `is_empty()` | 是否为空 |
| `size()` | 队列元素个数 |
| `__str__()` | 打印队列内容 |

> **注意**：Queue 用 list 实现的话，dequeue 时用 `pop(0)` 是 O(n)。先实现出来，然后思考：为什么标准库用 `deque` 而不是 `list`？

---

## 三、LeetCode 20 — 有效的括号（25min）

**题目**：判断括号是否合法配对
- `"()[]{}"` → True
- `"([)]"` → False
- `"{[]}"` → True

**思路**：这就是栈的经典应用！遇到左括号 push，遇到右括号 pop 检查是否匹配。

写到 `Day09_stack_queue.py` 末尾，加一个 `is_valid(s: str) -> bool` 函数。

---

## 四、英语（30min）

- **单词（15min）**：核心词 #1-25，见 `Day09_单词学习.txt`
- **听力（15min）**：VOA 常速 1 篇，精听（听不懂倒回去，直到每句都听清）

---

## 五、Git

```bash
cd E:\Users\MyFiles\Desktop\200day
git add .
git commit -m "Day9: 栈和队列 + LeetCode 20 有效括号"
git push
```

---

## 检查清单

- [ ] Stack 全部方法实现
- [ ] Queue 全部方法实现
- [ ] LeetCode 20 跑通
- [ ] 理解为什么队列用 deque 比 list 好
- [ ] 单词自测 ≥ 18/25
- [ ] VOA 听力 1 篇精听
- [ ] commit + push
