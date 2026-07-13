# Day 1（2026.07.08）— Python 基础夯实

> Phase 1 Week 1：列表推导式、dict/set、函数、异常处理、文件IO
> 今日主题：**列表推导式 + 字典/集合**

---

## 英语 30min

| 时间段 | 任务 | 内容 |
|--------|------|------|
| 早/睡前 | **背单词 15min** | 下面30个六级高频词——看英文想中文意思（**不拼写**），记不住的拿笔写两遍 |
| 早/睡前 | **听力 15min** | 去 [VOA常速英语](https://www.51voa.com/) 找一篇1-2分钟的新闻，听3遍：第1遍盲听理解大意，第2遍看原文跟读，第3遍再盲听检查自己能听懂多少 |

#### 今日30词（Day 1 六级高频词）

> **学习方式**：先整体看一遍，然后用手遮住中文列，看英文说中文意思。说不出的做标记，第二轮重点复习标记词。
> **过关标准**：遮住中文，30个里至少 **24个能说出正确意思（80%）**。达不到就标记错词、复习、再测，直到通过。

| # | 英文 | 中文 |
|---|------|------|
| 1 | **abuse** | v./n. 滥用；虐待 |
| 2 | **access** | n. 通道；使用权 v. 访问 |
| 3 | **accommodate** | v. 容纳；适应；为……提供住宿 |
| 4 | **acknowledge** | v. 承认；确认收到 |
| 5 | **advocate** | v./n. 提倡；拥护者 |
| 6 | **aggressive** | a. 侵略的；好斗的；进取的 |
| 7 | **alternative** | n. 替代选择 a. 可替代的 |
| 8 | **ambiguous** | a. 模棱两可的；含糊的 |
| 9 | **anticipate** | v. 预期；期望；提前行动 |
| 10 | **appreciate** | v. 欣赏；感激；升值 |
| 11 | **assess** | v. 评估；评定 |
| 12 | **assume** | v. 假定；承担；呈现出 |
| 13 | **attribute** | v. 归因于 n. 属性 |
| 14 | **barrier** | n. 障碍；屏障 |
| 15 | **capacity** | n. 容量；能力；职位 |
| 16 | **circumstance** | n. 情况；环境（常用复数） |
| 17 | **commitment** | n. 承诺；投入；奉献 |
| 18 | **compensate** | v. 补偿；赔偿 |
| 19 | **component** | n. 组成部分；部件 |
| 20 | **comprehensive** | a. 全面的；综合的 |
| 21 | **consequence** | n. 结果；后果；重要性 |
| 22 | **conservative** | a. 保守的 n. 保守派 |
| 23 | **consume** | v. 消费；消耗；吞噬 |
| 24 | **controversial** | a. 有争议的 |
| 25 | **convince** | v. 说服；使确信 |
| 26 | **coordinate** | v. 协调 n. 坐标 |
| 27 | **demonstrate** | v. 演示；证明；展示 |
| 28 | **depression** | n. 抑郁；萧条；洼地 |
| 29 | **distinguish** | v. 区分；辨别 |
| 30 | **domestic** | a. 国内的；家庭的；驯养的 |

#### 自测记录

- [ ] 第1轮：答对 ___ / 30（≥24 过关）  
- [ ] 补测（如有）：答对 ___ / ___（错词重新过关）

---

## AI 开发 90min

### 第一部分：知识点复习（60min）

按顺序敲完以下代码，**全部手打，不要复制粘贴**。每个小节跑通再进入下一节。

#### 1. 列表推导式（20min）

```python
# 基础写法
squares = [x**2 for x in range(10)]
print(squares)

# 带条件过滤
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# 嵌套循环
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)

# 实战：把一个句子中长度>3的单词全部大写
sentence = "hello world this is a python learning day"
long_words = [w.upper() for w in sentence.split() if len(w) > 3]
print(long_words)
```

#### 2. 字典进阶（20min）

```python
# dict comprehension
word_length = {w: len(w) for w in sentence.split()}
print(word_length)

# 实战：统计一段文本中每个单词的出现次数
text = "apple banana apple orange banana apple"
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1  # get的默认值用法，常用！
print(freq)

# 按value排序
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_freq)
```

#### 3. 集合（10min）

```python
# 去重
nums = [1, 2, 2, 3, 3, 3, 4]
unique = set(nums)
print(unique)

# 集合运算
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("交集:", a & b)
print("并集:", a | b)
print("差集:", a - b)
print("对称差:", a ^ b)
```

#### 4. 综合小练习（10min）

把以下需求自己写出来（不要看答案，写完跑通就算过关）：

> 给定一个列表 `[1, 1, 2, 3, 4, 4, 5, 6, 6, 6]`：
> 1. 用集合去重
> 2. 用字典统计每个数字出现的次数
> 3. 用列表推导式找出所有出现次数 >= 2 的数字

<details>
<summary>参考答案（做完再看）</summary>

```python
nums = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6]

# 1. 去重
unique = list(set(nums))
print("去重:", unique)

# 2. 统计次数
count = {}
for n in nums:
    count[n] = count.get(n, 0) + 1
print("统计:", count)

# 3. 出现次数 >= 2 的数字
duplicates = [n for n, c in count.items() if c >= 2]
print("重复:", duplicates)
```

</details>

---

### 第二部分：笔记 + GitHub 提交（15min）

1. 在桌面新建学习目录：`D:\Users\MyFiles\Desktop\AI-learning\`
2. 把今天写的代码保存为 `Day01_list_dict_set.py`
3. 初始化 Git 仓库并提交：

```bash
cd D:\Users\MyFiles\Desktop\AI-learning
git init
git add Day01_list_dict_set.py
git commit -m "Day01: 列表推导式、字典、集合复习"
```

4. 去 [github.com](https://github.com) 新建一个仓库叫 `ai-learning-200`（建议设为私有），然后：

```bash
git remote add origin https://github.com/你的用户名/ai-learning-200.git
git branch -M main
git push -u origin main
```

---

### 今日要记住的要点

| 要点 | 为什么重要 |
|------|-----------|
| `dict.get(key, default)` | 统计/计数场景极度常用，面试高频 |
| 列表推导式 `[expr for x in iterable if cond]` | Python 的招牌语法，代码简洁度的标志 |
| `sorted(d.items(), key=lambda x: x[1])` | 字典排序，项目里经常用到 |
| `set()` 去重 + 集合运算 | 数据处理的基本功 |

---

## 今日打卡清单

- [ ] 30个六级单词自测 ≥ 24分（未通过则补测直到通过）
- [ ] 精听1篇 VOA 常速新闻
- [ ] 手敲了列表推导式、字典、集合的所有代码
- [ ] 独立完成了综合小练习
- [ ] 代码 push 到了 GitHub
- [ ] 新建了 `AI-learning` 学习目录

---

> **如果今天太忙**：至少保证 30min 英语 + 1 个 GitHub commit（哪怕只提交几行代码+笔记），断一天容易断一周。
>
> 完成后告诉我，帮你准备 Day 2 的内容。加油 💪
