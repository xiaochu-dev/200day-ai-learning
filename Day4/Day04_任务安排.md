# Day 4（2026.07.15）— 面向对象进阶：继承与多态

> Phase 1 Week 2：类/继承/装饰器/生成器/import机制
> 今日主题：**继承、方法重写、多态、私有属性**

---

## 英语 30min

| 时间段 | 任务 | 内容 |
|--------|------|------|
| 早/睡前 | **背单词 15min** | 下面30个六级高频词——看英文想中文意思（**不拼写**），记不住的拿笔写两遍 |
| 早/睡前 | **听力 15min** | 去 [VOA常速英语](https://www.51voa.com/) 找一篇1-2分钟的新闻，听3遍：第1遍盲听理解大意，第2遍看原文跟读，第3遍再盲听检查自己能听懂多少 |

#### 今日30词（Day 4 六级高频词 #91-120）

> **Day 1-3 复习**：先花3分钟快速过一遍前三天的90个词（遮中文说意思），忘记的标记一下。
> **学习方式**：先整体看一遍，然后用手遮住中文列，看英文说中文意思。说不出的做标记，第二轮重点复习标记词。
> **过关标准**：遮住中文，30个里至少 **24个能说出正确意思（80%）**。达不到就标记错词、复习、再测，直到通过。

| # | 英文 | 中文 |
|---|------|------|
| 1 | **abandon** | v. 放弃；抛弃 |
| 2 | **abstract** | a. 抽象的 n. 摘要 |
| 3 | **academy** | n. 学院；学术机构 |
| 4 | **accommodate** | v. 容纳；为……提供住宿；适应 |
| 5 | **accompany** | v. 陪伴；伴随；为……伴奏 |
| 6 | **accomplish** | v. 完成；实现 |
| 7 | **acknowledge** | v. 承认；确认收到；感谢 |
| 8 | **acquire** | v. 获得；习得（语言/技能） |
| 9 | **adapt** | v. 适应；改编 |
| 10 | **adequate** | a. 足够的；适当的 |
| 11 | **adjust** | v. 调整；适应 |
| 12 | **administration** | n. 管理；行政；政府 |
| 13 | **adolescent** | n. 青少年 a. 青春期的 |
| 14 | **advocate** | v. 提倡 n. 倡导者 |
| 15 | **affair** | n. 事务；事件；私事 |
| 16 | **aggressive** | a. 侵略的；好斗的；有进取心的 |
| 17 | **allocate** | v. 分配；拨出 |
| 18 | **alternative** | n. 替代方案 a. 替代的 |
| 19 | **ambiguous** | a. 模棱两可的；含糊的 |
| 20 | **ambitious** | a. 有雄心的；野心勃勃的 |
| 21 | **annual** | a. 每年的 n. 年刊 |
| 22 | **anticipate** | v. 预期；期望；抢先 |
| 23 | **apparent** | a. 明显的；表面上的 |
| 24 | **appreciate** | v. 欣赏；感激；升值 |
| 25 | **approach** | v. 接近 n. 方法；途径 |
| 26 | **appropriate** | a. 适当的 v. 挪用；拨款 |
| 27 | **approximate** | a. 大约的 v. 接近 |
| 28 | **arise** | v. 出现；产生（arose, arisen） |
| 29 | **artificial** | a. 人工的；人造的；虚假的 |
| 30 | **assign** | v. 分配；指派；布置（作业） |

#### 自测记录

- [x] 第1轮：答对 15 / 30（≥24 过关）❌
- [x] 补测 第2轮：答对 12 / 15
- [x] 补测 第3轮：答对 3 / 3 ✅

---

## AI 开发 90min

### 今日概述

Day 3 学了怎么定义一个类。今天学**继承**——面向对象三大特性中最重要的一个（另两个是封装和多态，今天一起搞定）。

> **核心思想**：子类自动拥有父类的所有属性和方法，然后可以添加自己的东西或修改父类的行为。就像你继承了父母的一些特征，但又有自己独特的个性。

---

### 第一部分：知识点学习（60min）

按顺序敲完以下代码，**全部手打，不要复制粘贴**。每个小节跑通再进入下一节。

#### 1. 单继承 + `super().__init__()`（20min）

```python
# === 回顾：Day 3 的 Student 类 ===
class Student:
    school = "浙江工商大学"

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁，分数{self.score}"

    def get_grade(self):
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


# === 继承：定义子类 ===
# 语法：class 子类名(父类名):
class CollegeStudent(Student):
    """大学生——继承自 Student"""
    pass  # 什么都不写，完全继承父类


# 子类可以直接使用父类的一切
cs = CollegeStudent("张三", 20, 85)
print(cs.introduce())    # 我叫张三，今年20岁，分数85  ← 继承来的方法
print(cs.get_grade())    # 良好
print(cs.school)         # 浙江工商大学  ← 继承来的类属性
print(isinstance(cs, CollegeStudent))  # True
print(isinstance(cs, Student))         # True ← 子类实例也是父类实例！


# === super().__init__()：子类添加自己的属性 ===
class CollegeStudent(Student):
    """大学生——增加专业和年级"""

    def __init__(self, name, age, score, major, year):
        # super() 代表父类，super().__init__() 调用父类的初始化方法
        super().__init__(name, age, score)  # 先让父类处理 name, age, score
        self.major = major   # 子类自己的属性
        self.year = year     # 大一/大二/大三/大四

    def introduce(self):
        """重写父类的 introduce，加上专业和年级"""
        # 可以调用父类的方法拿到基础信息，再拼接
        base = super().introduce()
        return f"{base}，{self.major}专业，大{self.year}"


cs1 = CollegeStudent("张三", 20, 85, "计算机科学", 2)
cs2 = CollegeStudent("李四", 21, 92, "数学", 3)

print(cs1.introduce())
# 我叫张三，今年20岁，分数85，计算机科学专业，大二

print(cs2.get_grade())  # 优秀 —— 继承来的方法依然可用
```

#### 2. 方法重写（Override）（15min）

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        """评分标准：百分制"""
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

    def study(self):
        """学习行为——父类通用版本"""
        return f"{self.name} 在学习..."

    def __str__(self):
        return f"Student({self.name}, {self.age}岁)"


# === 子类重写方法 ===
class CollegeStudent(Student):
    def __init__(self, name, age, score, major):
        super().__init__(name, age, score)
        self.major = major

    def get_grade(self):
        """大学评分标准不同：改用 GPA 等级"""
        if self.score >= 90:
            return "A (4.0)"
        elif self.score >= 85:
            return "A- (3.7)"
        elif self.score >= 82:
            return "B+ (3.3)"
        elif self.score >= 78:
            return "B (3.0)"
        elif self.score >= 75:
            return "B- (2.7)"
        elif self.score >= 72:
            return "C+ (2.3)"
        elif self.score >= 68:
            return "C (2.0)"
        elif self.score >= 64:
            return "C- (1.7)"
        elif self.score >= 60:
            return "D (1.0)"
        else:
            return "F (0.0) 不及格"

    def study(self):
        """大学生学习行为——重写"""
        return f"{self.name}（{self.major}专业）在图书馆自习..."


class HighSchoolStudent(Student):
    def __init__(self, name, age, score, grade_level):
        super().__init__(name, age, score)
        self.grade_level = grade_level  # 高一/高二/高三

    def study(self):
        """高中生学习行为——重写"""
        return f"{self.name} 在备战高考，刷{self.grade_level}的题..."


# 同一个方法名，不同类的实例表现出不同行为
s1 = CollegeStudent("张三", 20, 85, "计算机")
s2 = HighSchoolStudent("小明", 17, 90, "高三")
s3 = Student("王五", 19, 78)  # 普通学生

print(s1.study())  # 张三（计算机专业）在图书馆自习...
print(s2.study())  # 小明 在备战高考，刷高三的题...
print(s3.study())  # 王五 在学习...

print(s1.get_grade())  # B+ (3.3)  ← 大学评分标准
print(s2.get_grade())  # 良好        ← 继承的父类评分标准（高中生没重写）
```

#### 3. 多态（Polymorphism）（15min）

```python
# === 多态的核心：同一个接口，不同的实现 ===
# 只要对象有同名方法，就可以用同一套代码处理

class Cat:
    def speak(self):
        return "喵喵喵 🐱"

class Dog:
    def speak(self):
        return "汪汪汪 🐶"

class Duck:
    def speak(self):
        return "嘎嘎嘎 🦆"

    def swim(self):
        return "鸭子在水里游"


# 多态函数：不关心参数是什么类型，只要它有 speak() 方法就行
def animal_chorus(animals):
    """动物合唱团——接受任何有 speak() 方法的对象"""
    for animal in animals:
        print(animal.speak())


# 三种完全不同的类，都可以传给同一个函数
animal_chorus([Cat(), Dog(), Duck(), Cat()])
# 喵喵喵 🐱
# 汪汪汪 🐶
# 嘎嘎嘎 🦆
# 喵喵喵 🐱


# === 多态在 OOP 里的经典用法 ===
# 前面的 Student 体系就是多态：
def print_study_session(students):
    """打印一群学生的学习情况——多态"""
    for s in students:
        print(f"  {s.study()}  → 成绩：{s.get_grade()}")


students = [
    CollegeStudent("张三", 20, 85, "计算机"),
    HighSchoolStudent("小明", 17, 90, "高三"),
    Student("王五", 19, 78),
    CollegeStudent("李四", 21, 92, "数学"),
]
print_study_session(students)
# 输出各不相同——同一个 study() 调用，不同类给出不同结果


# === isinstance() 与多态 ===
print(isinstance(Cat(), Cat))    # True
print(isinstance(Cat(), Dog))    # False
print(isinstance(Cat(), object)) # True —— 所有类最终都继承自 object

# 判断是否"某种类型"
def identify(obj):
    if isinstance(obj, Cat):
        print(f"这是一只猫：{obj.speak()}")
    elif isinstance(obj, Dog):
        print(f"这是一只狗：{obj.speak()}")
    else:
        print(f"未知动物：{obj.speak()}")

identify(Cat())
identify(Dog())
identify(Duck())
```

#### 4. 私有属性与方法（10min）

```python
# === Python 的"私有"约定 ===
# Python 没有真正的 private，靠命名约定来区分"公开"和"内部"

class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name              # 公开属性
        self._balance = balance       # _ 单下划线："protected"，约定不要直接访问
        self.__pin = pin              # __ 双下划线：名称改写（name mangling），更难直接访问

    def deposit(self, amount):
        """公开方法——外部可以调用"""
        if amount > 0:
            self._balance += amount
            return self._balance
        raise ValueError("金额必须 > 0")

    def get_balance(self):
        """公开的 getter——推荐通过方法访问 _balance"""
        return self._balance

    def _calculate_interest(self):
        """受保护方法——约定：子类和内部使用，外部不应调用"""
        return self._balance * 0.003  # 年利率 0.3%

    def __verify_pin(self, pin):
        """私有方法——名称改写为 _BankAccount__verify_pin"""
        return self.__pin == pin

    def withdraw(self, amount, pin):
        """取款需要密码验证"""
        if not self.__verify_pin(pin):
            return "密码错误，取款失败"
        if amount > self._balance:
            return "余额不足"
        self._balance -= amount
        return f"取款成功，余额 ¥{self._balance}"


acc = BankAccount("张三", 10000, pin="1234")

# 公开访问 OK
print(acc.name)           # 张三
print(acc.get_balance())  # 10000
acc.deposit(500)

# _balance 虽然可以访问，但约定告诉你"别碰"
print(acc._balance)       # 10500 —— 能访问，但你不应该这样做

# __pin 被名称改写，直接访问会报错
# print(acc.__pin)        # ❌ AttributeError!
# print(acc.__verify_pin("1234"))  # ❌ AttributeError!

# 但并非完全不能访问（Python 的哲学：我们都是成年人）
print(acc._BankAccount__pin)  # '1234' —— 知道规则就能访问，但这说明你在做坏事 😈

# 推荐的访问方式：通过公开方法
print(acc.withdraw(500, "1234"))   # 取款成功，余额 ¥10000
print(acc.withdraw(500, "0000"))   # 密码错误，取款失败
```

---

### 第二部分：综合练习（做完才看答案）

> **练习：扩展学生管理系统**
>
> 基于 Day 3 的 Student 类，构建一个继承体系：
>
> ```
> Person（基类）
> ├── 属性：name, age
> ├── 方法：introduce() → "我叫{name}，{age}岁"
> └── Student（继承 Person）
>     ├── 属性：+student_id, scores（成绩列表）
>     ├── 方法：+average_score()→平均分, +get_grade()→等级
>     └── Monitor（继承 Student，班长）
>         ├── 属性：+duty（职责描述）
>         └── 方法：重写 introduce()→ 加上"我是班长"
> ```
>
> 要求：
> 1. Person 有属性 `name`, `age`，方法 `introduce()`
> 2. Student 继承 Person，增加 `student_id`（学号）和 `scores`（成绩列表）
>    - `average_score()` 返回平均分
>    - `get_grade()` 根据平均分返回等级（和 Day 3 一样）
>    - 重写 `introduce()` 加上学号和平均分
> 3. Monitor 继承 Student，增加 `duty`（职责）
>    - 重写 `introduce()` 加上"我是班长，负责{duty}"
> 4. 创建2个普通学生 + 1个班长，调用各自方法验证

<details>
<summary>参考答案（做完再看）</summary>

```python
class Person:
    """基类：人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"我叫{self.name}，{self.age}岁"


class Student(Person):
    """学生——继承自 Person"""

    def __init__(self, name, age, student_id, scores=None):
        super().__init__(name, age)
        self.student_id = student_id
        self.scores = scores if scores is not None else []

    def average_score(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def get_grade(self):
        avg = self.average_score()
        if avg >= 90:
            return "优秀"
        elif avg >= 80:
            return "良好"
        elif avg >= 70:
            return "中等"
        elif avg >= 60:
            return "及格"
        else:
            return "不及格"

    def introduce(self):
        base = super().introduce()
        avg = self.average_score()
        return f"{base}，学号{self.student_id}，平均分{avg:.1f}（{self.get_grade()}）"


class Monitor(Student):
    """班长——继承自 Student"""

    def __init__(self, name, age, student_id, scores, duty):
        super().__init__(name, age, student_id, scores)
        self.duty = duty

    def introduce(self):
        base = super().introduce()
        return f"{base}，我是班长，负责{self.duty}"


# === 测试 ===
if __name__ == "__main__":
    s1 = Student("张三", 20, "S2024001", [85, 92, 78, 90])
    s2 = Student("李四", 21, "S2024002", [60, 55, 58, 62])
    monitor = Monitor("王五", 20, "S2024003", [95, 88, 92, 96], "考勤和班级事务")

    for person in [s1, s2, monitor]:
        print(person.introduce())

    # 类型检查
    print()
    print(f"monitor 是 Monitor 实例？{isinstance(monitor, Monitor)}")    # True
    print(f"monitor 是 Student 实例？{isinstance(monitor, Student)}")    # True
    print(f"monitor 是 Person 实例？{isinstance(monitor, Person)}")      # True
    print(f"monitor 是 object 实例？{isinstance(monitor, object)}")      # True

    # 班长也可以调用 Student 的方法
    print(f"班长平均分：{monitor.average_score():.1f}")
    print(f"班长等级：{monitor.get_grade()}")
```

</details>

---

### 第三部分：笔记 + GitHub 提交（10min）

1. 把今天写的代码保存为 `Day04_inheritance_polymorphism.py`
2. 提交并推送：

```bash
cd 你的项目目录
git add Day4
git commit -m "Day04: 面向对象进阶——继承、重写、多态、私有属性"
git push
```

> **提示**：如果你还没有在桌面初始化 git 仓库，今天用 `git init` 初始化，然后把 Day1-4 的文件都加进去。

---

### 今日要记住的要点

| 要点 | 为什么重要 |
|------|-----------|
| `class Child(Parent)` | 继承语法，子类获得父类的一切 |
| `super().__init__()` | 调用父类构造方法——**几乎所有子类 `__init__` 第一行都该调用它** |
| 方法重写（Override） | 子类可以改变父类方法的行为——不改父类、只改子类，开闭原则的基础 |
| 多态 | "同一个接口，不同实现"——`for obj in list: obj.do_something()` 不关心 obj 的具体类型 |
| `_attr` 单下划线 | 约定：受保护，子类和内部用，外部最好别碰 |
| `__attr` 双下划线 | 名称改写为 `_ClassName__attr`，避免子类意外覆盖 |
| `isinstance(obj, Class)` | 判断继承关系——子类实例也是父类实例 |

---

## 今日打卡清单

- [x] 30个六级单词自测 ≥ 24分 + 花3分钟复习Day 1-3单词
- [ ] 精听1篇 VOA 常速新闻
- [ ] 手敲了单继承、super()、方法重写、多态、私有属性的所有代码
- [ ] 独立完成了 Person → Student → Monitor 三级继承练习
- [ ] 代码 push 到了 GitHub

---

## 今日提示

继承是 OOP 最强大的特性，但也是最容易被滥用的。

一个简单的判断标准：**"是一个（is-a）"关系才用继承**。
- ✅ `CollegeStudent` **是一个** `Student` → 用继承
- ✅ `Monitor` **是一个** `Student` → 用继承
- ❌ `Car` **有一个** `Engine` → 用组合（把 Engine 作为属性），别用继承

> 组合（Composition）比继承更灵活，Day 5 会深入讲。今天先掌握继承的基本用法。

完成后告诉我，帮你准备 Day 5 的内容。加油 💪
