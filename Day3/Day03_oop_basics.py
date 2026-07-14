"""
Day 3 — 面向对象编程入门
主题：类与对象基础
按顺序手打以下代码，每个小节跑通再进入下一节。
"""

# ============================================================
# 第1节：类的定义与实例化（15min）
# ============================================================

# TODO: 定义一个最简单的类 Student（用 pass 占位）
# TODO: 创建两个实例 s1, s2，打印 type(s1) 和 isinstance(s1, Student)


# TODO: 重新定义 Student 类，添加 __init__(self, name, age, score)
#       在 __init__ 中用 self.xxx 保存三个参数
#       创建实例时打印一句"创建了一个学生对象：{name}"
# TODO: 创建 s1("张三", 20, 85) 和 s2("李四", 21, 92)
# TODO: 打印 s1.name, s1.score, 以及 f"{s2.name}今年{s2.age}岁"

class Student:
    pass

s1=Student()
s2=Student()
print(type(s1))
print(isinstance(s1, Student))

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        print(f"创建了一个学生对象：{name}")
s1=Student("张三", 20, 85)
s2=Student("李四", 21, 92)
print(s1.name)
print(s1.score)
print(f"{s2.name}今年{s2.age}岁")

# ============================================================
# 第2节：实例方法（15min）
# ============================================================

# TODO: 为 Student 类添加三个方法：
#       introduce(self)  → 返回 "我叫{name}，今年{age}岁，分数{score}"
#       get_grade(self)  → >=90优秀 >=80良好 >=70中等 >=60及格 <60不及格
#       is_passed(self)  → 返回 score >= 60
# TODO: 创建两个学生，调用这三个方法并打印结果
class Student:
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
    def is_passed(self):
         return self.score >= 60
s1 = Student("张三", 20, 85)
s2 = Student("李四", 21, 58)
print(s1.introduce())
print(s1.get_grade())
print(s1.is_passed())
print(s2.introduce())
print(s2.get_grade())
print(s2.is_passed())

# ============================================================
# 第3节：特殊方法 __str__ 和 __repr__（10min）
# ============================================================

# TODO: 为 Student 添加 __str__   → "Student(张三, 20岁, 85分)"
# TODO: 为 Student 添加 __repr__  → "Student(name='张三', age=20, score=85)"
# TODO: 测试 print(s), str(s), repr(s)
# TODO: 创建一个列表 [Student("张三",20,85), Student("李四",21,92)] 并打印
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def __str__(self):
        return f"Student({self.name}, {self.age}岁, {self.score})分"
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, score={self.score})"

s=Student("张三", 20, 85)
print(s)
print(str(s))
print(repr(s))
students = [Student("张三", 20, 85),Student("李四", 21, 92)]
print(students)
# ============================================================
# 第4节：类属性 vs 实例属性（10min）
# ============================================================

# TODO: 为 Student 添加类属性 school = "浙江工商大学" 和 student_count = 0
# TODO: 在 __init__ 中让 Student.student_count += 1
# TODO: 创建三个学生，打印每个人的 school 和 Student.student_count
# TODO: 修改 Student.school = "浙江大学"，再打印每个人的 school
# TODO: 尝试 s1.school = "清华"，然后打印 s1.school, Student.school, s2.school
#       ——理解这个"坑"！
class Student:
    school="浙江工商大学"
    student_count = 0
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        Student.student_count += 1

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

    def is_passed(self):
        return self.score >= 60

    def __str__(self):
        return f"Student({self.name}, {self.age}岁, {self.score}分)"

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, score={self.score})"

s1 = Student("张三", 20, 85)
s2 = Student("李四", 21, 92)
s3 = Student("王五", 19, 78)
print(s1.school)
print(s2.school)
print(s3.school)
Student.school="浙江大学"
print(s1.school)
print(f"总共创建了{Student.student_count}个学生")
s1.school="清华"
print(s1.school)
print(s2.school)
print(s3.school)
# ============================================================
# 第5节：实战——定义 Course 类并组合使用（10min）
# ============================================================

# TODO: 定义 Course 类：__init__(self, name, teacher, max_students)
#       属性：name, teacher, max_students, enrolled=[]（空列表）
# TODO: 方法 add_student(self, student)：未满则添加，满了打印提示
# TODO: 方法 list_students(self)：列出所有学生姓名和等级
# TODO: 方法 __str__(self)：返回课程概况
# TODO: 创建1门课程 + 4个学生，测试选课（前3个成功，第4个满员）
class Course:
    def __init__(self, name, teacher, max_students):
        self.name = name
        self.teacher = teacher
        self.max_students = max_students
        self.enrolled = []
    def add_student(self, student):
        if len(self.enrolled) < self.max_students:
            self.enrolled.append(student)
            print(f"{student.name}成功选了{self.name}")
            return True
        else:
            print(f"{self.name}已满员,{student.name}选课失败")
            return False
    def list_students(self):
        print(f"「{self.name}」学生名单（{len(self.enrolled)}/{self.max_students}）：")
        for s in self.enrolled:
            print(f"  - {s.name} ({s.get_grade()})")
    def __str__(self):
        return f"Course({self.name}, 教师={self.teacher}, {len(self.enrolled)}/{self.max_students}人)"

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
# ============================================================
# 综合练习：BankAccount 银行账户类
# ============================================================

# TODO: 定义 BankAccount 类
#       __init__(self, name, balance=0.0)
#       deposit(self, amount)    — 金额必须>0，否则 raise ValueError
#       withdraw(self, amount)   — 金额必须>0，余额不足 raise ValueError
#       transfer_to(self, other, amount) — 扣自己，加对方
#       __str__(self)            — "账户[张三]: 余额 ¥XX.XX"
#
# TODO: 创建两个账户，测试存款、取款、转账、异常情况
class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"存款金额必须 > 0，收到: {amount}")
        self.balance += amount
        print(f"{self.name} 存入 ¥{amount:.2f}，当前余额 ¥{self.balance:.2f}")
        return self.balance
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"取款金额必须 > 0，收到: {amount}")
        if amount > self.balance:
            raise ValueError(f"余额不足！余额 ¥{self.balance:.2f}，尝试取款 ¥{amount:.2f}")
        self.balance -= amount
        print(f"{self.name} 取出 ¥{amount:.2f}，当前余额 ¥{self.balance:.2f}")
        return self.balance
    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("转账目标必须是 BankAccount 实例")
        self.withdraw(amount)  # 先扣自己的（余额不足会抛异常）
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


# ============================================================
# 参考答案在 Day03_任务安排.md 的最后，做完再看！
# ============================================================
