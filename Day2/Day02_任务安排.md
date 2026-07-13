# Day 2（2026.07.09）— Python 函数与文件处理

> Phase 1 Week 1：列表推导式、dict/set、函数、异常处理、文件IO
> 今日主题：**函数 + 异常处理 + 文件IO**

---

## 英语 30min

| 时间段 | 任务 | 内容 |
|--------|------|------|
| 早/睡前 | **背单词 15min** | 下面30个六级高频词——看英文想中文意思（**不拼写**），记不住的拿笔写两遍 |
| 早/睡前 | **听力 15min** | ⚠️ Day 1 没做完，今天补上！去 [VOA常速英语](https://www.51voa.com/) 找一篇1-2分钟的新闻，听3遍：第1遍盲听理解大意，第2遍看原文跟读，第3遍再盲听检查自己能听懂多少 |

#### 今日30词（Day 2 六级高频词）

> **Day 1 复习**：先花2分钟快速过一遍昨天的30个词（遮中文说意思），忘记的标记一下。
> **学习方式**：先整体看一遍，然后用手遮住中文列，看英文说中文意思。说不出的做标记，第二轮重点复习标记词。
> **过关标准**：遮住中文，30个里至少 **24个能说出正确意思（80%）**。达不到就标记错词、复习、再测，直到通过。

| # | 英文 | 中文 |
|---|------|------|
| 1 | **dramatic** | a. 戏剧性的；巨大的；引人注目的 |
| 2 | **eliminate** | v. 消除；淘汰 |
| 3 | **emerge** | v. 出现；浮现；显露 |
| 4 | **emphasis** | n. 强调；重点 |
| 5 | **encounter** | v./n. 遭遇；遇到 |
| 6 | **enhance** | v. 增强；提高 |
| 7 | **enormous** | a. 巨大的；庞大的 |
| 8 | **equivalent** | a. 等价的 n. 等价物 |
| 9 | **evaluate** | v. 评估；评价 |
| 10 | **eventually** | ad. 最终；终于 |
| 11 | **evident** | a. 明显的；显然的 |
| 12 | **exceed** | v. 超过；超越 |
| 13 | **explicit** | a. 明确的；直截了当的 |
| 14 | **exploit** | v. 开发；利用；剥削 |
| 15 | **external** | a. 外部的；外界的 |
| 16 | **facilitate** | v. 促进；使便利 |
| 17 | **flexible** | a. 灵活的；柔韧的 |
| 18 | **fluctuate** | v. 波动；起伏 |
| 19 | **fundamental** | a. 基本的；根本的 n. 基本原理 |
| 20 | **generate** | v. 产生；生成 |
| 21 | **guarantee** | v./n. 保证；担保 |
| 22 | **identical** | a. 完全相同的；同一的 |
| 23 | **illustrate** | v. 阐明；举例说明 |
| 24 | **implement** | v. 实施；执行 |
| 25 | **implicit** | a. 含蓄的；隐含的；不明显的 |
| 26 | **inevitable** | a. 不可避免的 |
| 27 | **infrastructure** | n. 基础设施 |
| 28 | **innovation** | n. 创新；革新 |
| 29 | **investigate** | v. 调查；研究 |
| 30 | **justify** | v. 证明……正当；为……辩护 |

#### 自测记录

- [x] 第1轮：答对 17 / 30（未达标）  
- [x] 补测第2轮：答对 6 / 13（错词+漏词）  
- [x] 补测第3轮：答对 6 / 7（达标 ✅）  
- [ ] ⚠️ 还剩 1 个易混词：**explicit**（明确的）≠ evident（显然的）

---

## AI 开发 90min

### 第一部分：知识点复习（60min）

按顺序敲完以下代码，**全部手打，不要复制粘贴**。每个小节跑通再进入下一节。

#### 1. 函数基础（20min）

```python
# === 基本定义与调用 ===
def greet(name):
    """向指定的人打招呼"""  # 这是docstring，用help(greet)可以看到
    return f"Hello, {name}!"

print(greet("World"))
print(greet.__doc__)  # 打印函数的文档字符串

# === 默认参数 ===
def power(base, exp=2):
    """计算base的exp次方，默认平方"""
    return base ** exp

print(power(3))      # 9（使用默认值）
print(power(3, 3))   # 27

# ⚠️ 默认参数的坑：不要在默认值里用可变对象！
# 错误示范：def add_item(item, lst=[]):  -> 多次调用会共享同一个list
# 正确做法：
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [2]  ← 正确！不会残留上一次的结果

# === 多种调用方式 ===
def describe_person(name, age, city="未知"):
    return f"{name}, {age}岁, 来自{city}"

# 位置参数
print(describe_person("张三", 20))
# 关键字参数（顺序可变）
print(describe_person(age=22, name="李四"))
# 混合使用
print(describe_person("王五", 25, city="杭州"))
```

#### 2. 高级参数与返回值（15min）

```python
# === *args：接收任意数量的位置参数 ===
def my_sum(*args):
    """接收任意数量的数字并求和"""
    total = 0
    for n in args:
        total += n
    return total

print(my_sum(1, 2, 3))       # 6
print(my_sum(1, 2, 3, 4, 5)) # 15

# === **kwargs：接收任意数量的关键字参数 ===
def build_profile(**kwargs):
    """构建个人信息字典"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user = build_profile(name="Alice", age=25, job="Engineer")
print(user)  # {'name': 'Alice', 'age': 25, 'job': 'Engineer'}

# === 两者结合 ===
def log_info(level, *args, **kwargs):
    """模拟日志输出"""
    print(f"[{level}]", " ".join(str(a) for a in args))
    if kwargs:
        print("  附加信息:", kwargs)

log_info("INFO", "用户", "登录", ip="192.168.1.1", port=8080)

# === lambda 匿名函数 ===
# 用于简单的、一次性的操作
nums = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(nums, key=lambda x: -x)  # 按降序排列
print(sorted_nums)

# lambda 配合 map/filter
doubled = list(map(lambda x: x * 2, nums))
evens_only = list(filter(lambda x: x % 2 == 0, nums))
print("翻倍:", doubled)
print("偶数:", evens_only)
```

#### 3. 异常处理（12min）

```python
# === 基本 try/except ===
def safe_divide(a, b):
    """安全除法，处理除零和类型错误"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：不能除以零！")
        return None
    except TypeError:
        print("错误：操作数类型不正确！")
        return None
    else:
        # 没有异常时执行
        print(f"{a} / {b} = {result}")
        return result
    finally:
        # 无论是否异常都执行（常用于清理资源）
        print("safe_divide 执行完毕")

print(safe_divide(10, 2))  # 正常
print(safe_divide(10, 0))  # 除零异常
print()

# === 实战：读取文件时的异常处理 ===
def read_file_safe(filepath):
    """安全读取文件内容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件不存在：{filepath}")
        return None
    except PermissionError:
        print(f"没有权限读取：{filepath}")
        return None
    except Exception as e:
        # 捕获其他所有意料之外的异常
        print(f"读取文件时发生未知错误：{e}")
        return None

# 试一下（这个文件应该不存在）
content = read_file_safe("不存在的文件.txt")
```

#### 4. 文件IO（13min）

```python
# === 写文件 ===
# 'w' 模式会覆盖已有文件，'a' 模式追加到末尾
poem = """春眠不觉晓，
处处闻啼鸟。
夜来风雨声，
花落知多少。"""

with open("poem.txt", "w", encoding="utf-8") as f:
    f.write(poem)
print("已写入 poem.txt")

# === 读文件（一次性读全部）===
with open("poem.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("文件内容：")
print(content)

# === 逐行读取 ===
print("逐行读取：")
with open("poem.txt", "r", encoding="utf-8") as f:
    for line_no, line in enumerate(f, 1):
        print(f"  第{line_no}行：{line.strip()}")

# === 读成列表（每行一个元素）===
with open("poem.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"\n总共 {len(lines)} 行")

# === 追加写入 ===
with open("poem.txt", "a", encoding="utf-8") as f:
    f.write("\n--- 古诗一首 ---")
print("已追加署名")

# === CSV 文件实战 ===
import csv

# 写入 CSV
with open("students.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "年龄", "分数"])
    writer.writerow(["张三", 20, 85])
    writer.writerow(["李四", 21, 92])
    writer.writerow(["王五", 19, 78])
print("已写入 students.csv")

# 读取 CSV
with open("students.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['姓名']}: {row['年龄']}岁, {row['分数']}分")
```

---

### 第二部分：综合小练习（做完才看答案）

把以下需求自己写出来，跑通算过关：

> **练习 1**：写一个函数 `analyze_text(filepath)`，读取一个文本文件，返回：
> - 总单词数
> - 不同单词数
> - 出现次数最多的3个单词（及其次数）
>
> **练习 2**：写一个函数 `save_student_scores(filepath, scores_dict)`，把 `{"张三": 85, "李四": 92, "王五": 78}` 保存为 CSV 文件，包含"姓名""分数""等级"三列（≥90→优秀，≥80→良好，≥70→中等，<70→加油）。用 try/except 处理文件写入异常。

> 提示：综合用到今天学的函数、文件IO、异常处理，以及 Day 1 的字典和列表推导式。

<details>
<summary>参考答案（做完再看）</summary>

```python
import csv
from collections import Counter

def analyze_text(filepath):
    """分析文本文件的单词统计"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"文件不存在：{filepath}")
        return None
    
    # 清理文本：转小写，按空格分割
    words = text.lower().split()
    # 去掉标点（简单处理）
    words = [w.strip('.,!?;:""()[]') for w in words if w.strip('.,!?;:""()[]')]
    
    total = len(words)
    unique = len(set(words))
    
    # 用 Counter 统计词频
    counter = Counter(words)
    top3 = counter.most_common(3)
    
    return {
        "总单词数": total,
        "不同单词数": unique,
        "前3高频词": top3
    }


def save_student_scores(filepath, scores_dict):
    """保存学生成绩到 CSV"""
    def get_grade(score):
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 70:
            return "中等"
        else:
            return "加油"
    
    try:
        with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(["姓名", "分数", "等级"])
            for name, score in scores_dict.items():
                writer.writerow([name, score, get_grade(score)])
        print(f"已保存到 {filepath}")
    except Exception as e:
        print(f"写入文件失败：{e}")


# === 测试 ===
if __name__ == "__main__":
    # 测试练习1：分析刚才创建的 poem.txt
    result = analyze_text("poem.txt")
    if result:
        for k, v in result.items():
            print(f"{k}: {v}")
    
    print()
    
    # 测试练习2
    save_student_scores("report.csv", {"张三": 85, "李四": 92, "王五": 78, "赵六": 65})
    print("请打开 report.csv 查看结果！")
```

</details>

---

### 第三部分：笔记 + GitHub 提交（15min）

1. 把今天写的代码保存为 `Day02_functions_exceptions_io.py`
2. 提交并推送：

```bash
cd D:\Users\MyFiles\Desktop\AI-learning
git add Day02_functions_exceptions_io.py
git commit -m "Day02: 函数、异常处理、文件IO"
git push
```

---

### 今日要记住的要点

| 要点 | 为什么重要 |
|------|-----------|
| `try/except/else/finally` 结构 | 程序健壮性的基础，面试必问 |
| `with open(...) as f:` | 上下文管理器，自动关闭文件，避免资源泄露 |
| `*args` 和 `**kwargs` | 灵活函数接口，源码阅读必备 |
| 默认参数不用可变对象 `[]` | 经典陷阱，几乎所有 Python 面试都会考 |
| `csv.DictReader` | 数据处理入门，后续爬虫/数据分析的基石 |
| lambda + map/filter | 函数式编程风格，代码简洁 |

---

## 今日打卡清单

- [ ] 30个六级单词自测 ≥ 24分 + 花2分钟复习Day 1单词
- [ ] 精听1篇 VOA 常速新闻（Day 1 欠的今天补上）
- [ ] 手敲了函数、异常处理、文件IO的所有代码
- [ ] 独立完成了2道综合小练习
- [ ] 代码 push 到了 GitHub

---

> **今日提示**：函数是编程的核心抽象手段。写函数时想想"这个函数的输入是什么？输出是什么？会不会有异常情况？"——养成这三个习惯，代码质量会大幅提升。
>
> 完成后告诉我，帮你准备 Day 3 的内容。加油 💪
