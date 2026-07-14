# Day 3（2026.07.14）— 面向对象编程入门

> Phase 1 Week 2：类/继承/装饰器/生成器/import机制
> 今日主题：**类与对象基础**

---

## 英语 30min

| 时间段 | 任务 | 内容 |
|--------|------|------|
| 早/睡前 | **背单词 15min** | 下面30个六级高频词——看英文想中文意思（**不拼写**），记不住的拿笔写两遍 |
| 早/睡前 | **听力 15min** | 去 [VOA常速英语](https://www.51voa.com/) 找一篇1-2分钟的新闻，听3遍：第1遍盲听理解大意，第2遍看原文跟读，第3遍再盲听检查自己能听懂多少 |

#### 今日30词（Day 3 六级高频词）

> **Day 1-2 复习**：先花3分钟快速过一遍前两天的60个词（遮中文说意思），忘记的标记一下。
> **学习方式**：先整体看一遍，然后用手遮住中文列，看英文说中文意思。说不出的做标记，第二轮重点复习标记词。
> **过关标准**：遮住中文，30个里至少 **24个能说出正确意思（80%）**。达不到就标记错词、复习、再测，直到通过。

| # | 英文 | 中文 |
|---|------|------|
| 1 | **maintain** | v. 维持；维护；坚持认为 |
| 2 | **mechanism** | n. 机制；机械装置 |
| 3 | **minority** | n. 少数；少数民族 |
| 4 | **negotiate** | v. 谈判；协商 |
| 5 | **nevertheless** | ad. 然而；不过 |
| 6 | **objective** | n. 目标 a. 客观的 |
| 7 | **obstacle** | n. 障碍；阻碍 |
| 8 | **occupation** | n. 职业；占领；消遣 |
| 9 | **participate** | v. 参与；参加 |
| 10 | **perceive** | v. 察觉；感知；理解 |
| 11 | **phenomenon** | n. 现象（复数 phenomena） |
| 12 | **potential** | a. 潜在的 n. 潜力 |
| 13 | **precisely** | ad. 精确地；恰好 |
| 14 | **predominant** | a. 占优势的；主导的 |
| 15 | **presumably** | ad. 大概；据推测 |
| 16 | **priority** | n. 优先事项；优先权 |
| 17 | **profound** | a. 深远的；深刻的 |
| 18 | **proportion** | n. 比例；部分 |
| 19 | **psychological** | a. 心理的；心理学的 |
| 20 | **pursue** | v. 追求；追逐；从事 |
| 21 | **rational** | a. 理性的；合理的 |
| 22 | **readily** | ad. 乐意地；容易地 |
| 23 | **register** | v./n. 登记；注册；显示 |
| 24 | **regulate** | v. 调节；管理；控制 |
| 25 | **reject** | v. 拒绝；排斥；驳回 |
| 26 | **release** | v./n. 释放；发布；解除 |
| 27 | **relevant** | a. 相关的；切题的 |
| 28 | **reluctant** | a. 不情愿的；勉强的 |
| 29 | **resolve** | v. 解决；决心 n. 决心 |
| 30 | **restrict** | v. 限制；约束 |

#### 自测记录

- [x] 第1轮：答对 15 / 30（≥24 过关）❌ 未达标
- [x] 补测 第2轮：答对 13 / 15 ✅ 达标
- [x] 补测 第3轮：答对 2 / 2 ✅ 全部通过

---

## AI 开发 90min

### 今日概述

Day 1 学了数据结构（list/dict/set），Day 2 学了函数和文件。今天开始 **面向对象编程（OOP）**——这是 Python 最重要的编程范式，也是面试必考内容。

> **核心思想**：把数据和操作数据的方法打包在一起，变成"对象"。比如一个"学生"对象，既有数据（姓名、年龄、分数），又有方法（计算等级、打印信息）。

---

### 第一部分：知识点学习（60min）

按顺序敲完以下代码，**全部手打，不要复制粘贴**。每个小节跑通再进入下一节。

#### 1. 类的定义与实例化（15min）

```python
# === 定义一个最简单的类 ===
class Student:
    """学生类"""  # 类的docstring
    pass  # 占位符，表示类体为空

# 创建实例（对象）
s1 = Student()
s2 = Student()
print(type(s1))    # <class '__main__.Student'>
print(isinstance(s1, Student))  # True

# === 带 __init__ 的类 ===
class Student:
    """学生类，包含姓名、年龄、分数"""

    def __init__(self, name, age, score):
        """初始化方法——创建对象时自动调用"""
        self.name = name   # self.name 是实例属性
        self.age = age
        self.score = score
        print(f"创建了一个学生对象：{name}")

# 创建实例时会自动调用 __init__
s1 = Student("张三", 20, 85)
s2 = Student("李四", 21, 92)

# 访问属性
print(s1.name)    # 张三
print(s1.score)   # 85
print(f"{s2.name}今年{s2.age}岁")  # 李四今年21岁
```

#### 2. 实例方法（15min）

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # === 实例方法（第一个参数永远是 self）===
    def introduce(self):
        """自我介绍"""
        return f"我叫{self.name}，今年{self.age}岁，分数{self.score}"

    def get_grade(self):
        """根据分数返回等级"""
        if self.score >= 90:
            return "优秀"
        elif self.score >= 80:
            return "良好"
        elif self.score >= 70:
            return "中等"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"

    def is_passed(self):
        """是否及格"""
        return self.score >= 60


# 使用
s1 = Student("张三", 20, 85)
s2 = Student("李四", 21, 58)

print(s1.introduce())   # 我叫张三，今年20岁，分数85
print(s1.get_grade())   # 良好
print(s1.is_passed())   # True

print(s2.introduce())   # 我叫李四，今年21岁，分数58
print(s2.get_grade())   # 不及格
print(s2.is_passed())   # False
```

#### 3. 特殊方法 `__str__` 和 `__repr__`（10min）

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        """给用户看的，用 print() 或 str() 时调用"""
        return f"Student({self.name}, {self.age}岁, {self.score}分)"

    def __repr__(self):
        """给开发者看的，调试时用；如果没定义 __str__ 则回退到 __repr__"""
        return f"Student(name='{self.name}', age={self.age}, score={self.score})"


s = Student("张三", 20, 85)

print(s)           # 调用 __str__ → Student(张三, 20岁, 85分)
print(str(s))      # 同上
print(repr(s))     # 调用 __repr__ → Student(name='张三', age=20, score=85)

# 在列表里会调用 __repr__
students = [Student("张三", 20, 85), Student("李四", 21, 92)]
print(students)    # [Student(name='张三', age=20, score=85), Student(name='李四', age=21, score=92)]
```

#### 4. 类属性 vs 实例属性（10min）

```python
class Student:
    # === 类属性：所有实例共享 ===
    school = "浙江工商大学"
    student_count = 0

    def __init__(self, name, age, score):
        # === 实例属性：每个实例各自持有 ===
        self.name = name
        self.age = age
        self.score = score
        # 每创建一个学生，类属性+1
        Student.student_count += 1


s1 = Student("张三", 20, 85)
s2 = Student("李四", 21, 92)
s3 = Student("王五", 19, 78)

# 所有学生共享同一个 school
print(s1.school)   # 浙江工商大学
print(s2.school)   # 浙江工商大学
print(s3.school)   # 浙江工商大学

# 改类属性——所有实例都受影响
Student.school = "浙江大学"
print(s1.school)   # 浙江大学

# 类属性统计实例数量
print(f"总共创建了{Student.student_count}个学生")  # 3

# ⚠️ 坑：通过实例修改类属性只会创建同名实例属性，不影响类属性！
s1.school = "清华"  # 这只是在 s1 上新建了一个实例属性 school
print(s1.school)           # 清华（实例属性盖住了类属性）
print(Student.school)      # 浙江大学（类属性没变！）
print(s2.school)           # 浙江大学（s2 没有自己的 school，还是读类属性）
```

#### 5. 实战：定义一个小型类系（10min）

```python
# 除了 Student，再定义一个 Course（课程）类
# 体会"类就是把相关的数据和操作打包"

class Course:
    def __init__(self, name, teacher, max_students):
        self.name = name
        self.teacher = teacher
        self.max_students = max_students
        self.enrolled = []  # 已选课的学生列表

    def add_student(self, student):
        """添加学生（如果未满）"""
        if len(self.enrolled) < self.max_students:
            self.enrolled.append(student)
            print(f"{student.name} 成功选了「{self.name}」")
            return True
        else:
            print(f"「{self.name}」已满员，{student.name} 选课失败")
            return False

    def list_students(self):
        """列出所有选课学生"""
        print(f"「{self.name}」学生名单（{len(self.enrolled)}/{self.max_students}）：")
        for s in self.enrolled:
            print(f"  - {s.name} ({s.get_grade()})")

    def __str__(self):
        return f"Course({self.name}, 教师={self.teacher}, {len(self.enrolled)}/{self.max_students}人)"


# === 组合使用 ===
# 创建课程
python_course = Course("Python程序设计", "王老师", max_students=3)

# 创建学生
s1 = Student("张三", 20, 85)
s2 = Student("李四", 21, 92)
s3 = Student("王五", 19, 78)
s4 = Student("赵六", 20, 55)

# 选课
python_course.add_student(s1)  # 成功
python_course.add_student(s2)  # 成功
python_course.add_student(s3)  # 成功
python_course.add_student(s4)  # 满员！

print()
python_course.list_students()
```

---

### 第二部分：综合小练习（做完才看答案）

> **练习**：写一个 `BankAccount`（银行账户）类，包含以下功能：
>
> 1. 初始化：账户名 `name`、初始余额 `balance`（默认0）
> 2. 方法 `deposit(amount)`：存款，金额必须 > 0，否则抛 `ValueError`
> 3. 方法 `withdraw(amount)`：取款，余额不足抛 `ValueError`，金额必须 > 0
> 4. 方法 `transfer_to(other_account, amount)`：转账给另一个 BankAccount，扣自己加对方
> 5. 定义 `__str__` 让它打印时显示 `账户[张三]: 余额 ¥XX.XX`
>
> 提示：用到 `__init__`、实例方法、`raise ValueError(...)`、`__str__`

<details>
<summary>参考答案（做完再看）</summary>

```python
class BankAccount:
    """银行账户类"""

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValueError(f"存款金额必须 > 0，收到: {amount}")
        self.balance += amount
        print(f"{self.name} 存入 ¥{amount:.2f}，当前余额 ¥{self.balance:.2f}")
        return self.balance

    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValueError(f"取款金额必须 > 0，收到: {amount}")
        if amount > self.balance:
            raise ValueError(f"余额不足！余额 ¥{self.balance:.2f}，尝试取款 ¥{amount:.2f}")
        self.balance -= amount
        print(f"{self.name} 取出 ¥{amount:.2f}，当前余额 ¥{self.balance:.2f}")
        return self.balance

    def transfer_to(self, other_account, amount):
        """转账给另一个账户"""
        if not isinstance(other_account, BankAccount):
            raise TypeError("转账目标必须是 BankAccount 实例")
        self.withdraw(amount)   # 先扣自己的（余额不足会抛异常）
        other_account.deposit(amount)  # 再加给对方的
        print(f"转账成功：{self.name} → {other_account.name}，¥{amount:.2f}")

    def __str__(self):
        return f"账户[{self.name}]: 余额 ¥{self.balance:.2f}"


# === 测试 ===
if __name__ == "__main__":
    a1 = BankAccount("张三", 1000)
    a2 = BankAccount("李四", 500)

    print(a1)
    print(a2)
    print()

    # 正常操作
    a1.deposit(200)
    a1.withdraw(150)
    a1.transfer_to(a2, 300)
    print()

    print(a1)
    print(a2)
    print()

    # 异常测试
    try:
        a1.withdraw(99999)  # 余额不足
    except ValueError as e:
        print(f"取款失败：{e}")

    try:
        a1.deposit(-50)     # 金额非法
    except ValueError as e:
        print(f"存款失败：{e}")
```

</details>

---

### 第三部分：笔记 + GitHub 提交（15min）

1. 把今天写的代码保存为 `Day03_oop_basics.py`
2. 提交并推送：

```bash
cd E:\Users\MyFiles\Desktop\200day
git add Day3
git commit -m "Day03: 面向对象基础——类、实例、方法、属性"
git push
```

---

### 今日要记住的要点

| 要点 | 为什么重要 |
|------|-----------|
| `self` 是什么 | 代表实例本身，调用 `s1.introduce()` 等价于 `Student.introduce(s1)` |
| `__init__` vs `__str__` | init 是初始化（创建时调用），str 是字符串表示（打印时调用） |
| 类属性 vs 实例属性 | 类属性所有实例共享（如 `school`），实例属性各自持有（如 `name`） |
| `raise ValueError(...)` | 主动抛出异常，让调用方处理——防御性编程的基本功 |
| `isinstance(obj, Class)` | 类型检查，写健壮代码时常用 |

---

## 今日打卡清单

- [ ] 30个六级单词自测 ≥ 24分 + 花3分钟复习Day 1-2单词
- [ ] 精听1篇 VOA 常速新闻
- [ ] 手敲了类定义、`__init__`、实例方法、`__str__`、类属性的所有代码
- [ ] 独立完成了 BankAccount 综合练习
- [ ] 代码 push 到了 GitHub

---

> **今日提示**：面向对象的第一道坎是理解 `self`。你可以这样想：`s1.introduce()` 其实就是 `Student.introduce(s1)`——Python 自动把 `.` 前面的对象作为第一个参数传进去。这个参数习惯上叫 `self`，但你可以叫任何名字（不过没人会改，改了会被同事打死 😄）。
>
> 完成后告诉我，帮你准备 Day 4 的内容。加油 💪
