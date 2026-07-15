"""
Day 4 — 面向对象进阶：继承与多态
主题：继承、方法重写、多态、私有属性
按顺序手打以下代码，每个小节跑通再进入下一节。
参考答案在 Day04_任务安排.md 里。
"""

# ============================================================
# 第1节：单继承 + super().__init__()（20min）
# ============================================================

# TODO: 定义一个 Student 基类（回顾 Day 3）
#       __init__(self, name, age, score)
#       类属性 school = "浙江工商大学"
#       方法 introduce(self) → "我叫{name}，今年{age}岁，分数{score}"
#       方法 get_grade(self) → 根据 score 返回等级
class Student:
    school = "浙江工商大学"
    def __init__(self, name, age,score):
        self.name = name
        self.age = age
        self.score = score
    def introduce(self):
        return f"我叫{self.name},今年{self.age}岁，分数{self.score}"
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

# TODO: 定义 CollegeStudent(Student)，先用 pass 占位
#       创建实例 cs = CollegeStudent("张三", 20, 85)
#       调用 cs.introduce() 和 cs.get_grade()，观察是否继承了父类方法
#       用 isinstance(cs, CollegeStudent) 和 isinstance(cs, Student) 验证
class CollegeStudent(Student):
    pass
cs = CollegeStudent("张三", 20, 85)
print(cs.introduce())
print(cs.get_grade())
print(cs.school)
print(isinstance(cs, CollegeStudent))
print(isinstance(cs, Student))
# TODO: 重写 CollegeStudent，添加 __init__(self, name, age, score, major, year)
#       使用 super().__init__(name, age, score) 调用父类的初始化
#       添加 self.major 和 self.year
#       重写 introduce() → 使用 super().introduce() 拼接专业和年级信息
class CollegeStudent(Student):
    def __init__(self, name, age, score,major,year):
        super().__init__(name, age, score)
        self.major = major
        self.year = year
    def introduce(self):
        base=super().introduce()
        return f"{base},{self.major}专业,大{self.year}"

cs1=CollegeStudent("张三",20,85,"计算机科学",2)
cs2=CollegeStudent("李四",21,92,"数学",3)
print(cs1.introduce())
print(cs2.get_grade())
# ============================================================
# 第2节：方法重写（Override）（15min）
# ============================================================

# TODO: 定义 Student 基类（带 get_grade 百分制 + study 方法 + __str__）
# TODO: 定义 CollegeStudent(Student)：重写 get_grade（改为GPA等级）、study（图书馆自习）
# TODO: 定义 HighSchoolStudent(Student)：只重写 study（备战高考），get_grade 继承父类
# TODO: 创建三个实例，打印 study() 和 get_grade()，对比输出差异

class Student:
    def __init__(self, name, age,score):
        self.name = name
        self.age = age
        self.score = score

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
    def study(self):
        return f"{self.name}在学习..."

    def __str__(self):
        return f"Student({self.name},{self.age}岁)"

class CollegeStudent(Student):
    def __init__(self, name, age, score,major):
        super().__init__(name, age, score)
        self.major = major
    def get_grade(self):
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
        return f"{self.name}({self.major}专业) 在图书馆自习..."

class HighSchoolStudent(Student):
    def __init__(self, name, age, score,grade_level):
        super().__init__(name, age, score)
        self.grade_level = grade_level
    def study(self):
        return f"{self.name}在备战高考，刷{self.grade_level}的题..."

s1=CollegeStudent("张三",20,85,"计算机")
s2=HighSchoolStudent("小明",17,90,"高三")
s3=Student("王五",19,78)

print(s1.study())
print(s2.study())
print(s3.study())

print(s1.get_grade())
print(s2.get_grade())
# ============================================================
# 第3节：多态（Polymorphism）（15min）
# ============================================================

# TODO: 定义三个类 Cat, Dog, Duck，每个都有 speak() 方法
# TODO: 写一个 animal_chorus(animals) 函数，遍历并调用 .speak()
# TODO: 测试：传入 [Cat(), Dog(), Duck(), Cat()]

# TODO: 写一个 print_study_session(students) 函数，遍历并打印 study() + get_grade()
# TODO: 传入 [CollegeStudent(...), HighSchoolStudent(...), Student(...), CollegeStudent(...)]

# TODO: 用 isinstance() 写一个 identify(obj) 函数，判断 Cat/Dog/其他
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

def animal_chorus(animals):
    for animal in animals:
        print(animal.speak())

animal_chorus([Cat(),Dog(),Duck(),Cat()])

def print_study_session(students):
    for s in students:
        print(f" {s.study()}→成绩:{s.get_grade()}")

students=[CollegeStudent("张三",20,85,"计算机"),
          HighSchoolStudent("小明",17,90,"高三"),
          Student("王五",19,78),
          CollegeStudent("李四",21,92,"数学")]
print_study_session(students)

print(isinstance(Cat(),Cat))
print(isinstance(Cat(),Dog))
print(isinstance(Cat(),object))

def identity(obj):
    if isinstance(obj,Cat):
        print(f"这是一只猫:{obj.speak()}")
    elif isinstance(obj,Dog):
        print(f"这是一只狗:{obj.speak()}")
    else:
        print(f"未知动物:{obj.speak()}")

identity(Cat())
identity(Dog())
identity(Duck())
# ============================================================
# 第4节：私有属性与方法（10min）
# ============================================================

# TODO: 定义 BankAccount 类
#       __init__(self, name, balance, pin)
#           self.name → 公开属性
#           self._balance → 受保护属性（单下划线约定）
#           self.__pin → 私有属性（双下划线，名称改写）
# TODO: 方法 deposit(self, amount) → 公开
# TODO: 方法 get_balance(self) → 公开的 getter
# TODO: 方法 _calculate_interest(self) → 受保护的（单下划线约定）
# TODO: 方法 __verify_pin(self, pin) → 私有的（双下划线）
# TODO: 方法 withdraw(self, amount, pin) → 公开，调用 __verify_pin 验证密码
# TODO: 测试：正常访问、尝试访问 __pin（报错）、通过 _BankAccount__pin 访问
class BankAccount:
    def __init__(self, name, balance,pin):
        self.name = name
        self._balance = balance
        self.__pin = pin
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        raise ValueError("金额必须>0")
    def get_balance(self):
        return self._balance
    def _calculate_interest(self):
        return self._balance * 0.003
    def __verify_pin(self,pin):
        return self.__pin == pin
    def withdraw(self, amount,pin):
        if not self.__verify_pin(pin):
            return "密码错误，取款失败"
        if amount > self._balance:
            return "余额不足"
        self._balance -= amount
        return f"取款成功,余额 ¥{self._balance}"

acc=BankAccount("张三",10000,pin="1234")

print(acc.name)
print(acc.get_balance())
acc.deposit(500)

print(acc._balance)

print(acc._BankAccount__pin)

print(acc.withdraw(500,"1234"))
print(acc.withdraw(500,"0000"))

# ============================================================
# 综合练习：Person → Student → Monitor 三级继承
# ============================================================

# TODO: Person 基类：__init__(self, name, age), introduce()
# TODO: Student(Person)：+student_id, scores
#       average_score() → 平均分
#       get_grade() → 等级
#       重写 introduce() → 加上学号和平均分
# TODO: Monitor(Student)：+duty
#       重写 introduce() → 加上"我是班长，负责{duty}"
# TODO: 创建2个普通学生 + 1个班长，调用 introduce() 验证

