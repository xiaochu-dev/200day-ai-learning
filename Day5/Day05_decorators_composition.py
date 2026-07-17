"""
Day 5 — 装饰器与组合
主题：装饰器、@property、组合 vs 继承
按顺序手打以下代码，每个小节跑通再进入下一节。
参考答案在 Day05_任务安排.md 里。
"""

# ============================================================
# 第1节：装饰器入门（20min）
# ============================================================

# TODO: 先理解函数也是对象——把函数赋值给变量，通过变量调用
# TODO: 不用装饰器，给 say_hello 和 say_bye 加日志（重复代码多）
def greet():
    return 'Hello!'

print(greet)
print(greet())

f=greet
print(f())

def say_hello():
    print('[LOG] 函数开始执行')
    print("Hello World")
    print('[LOG] 函数执行完毕')

def say_bye():
    print('[LOG] 函数开始执行')
    print("Goodbye")
    print('[LOG] 函数执行完毕')

say_hello()
say_bye()
# TODO: 写 log_decorator(func) 装饰器——接收函数，返回 wrapper
# TODO: wrapper 里先打印日志，再调用 func，最后再打印日志
def log_decorator(func):
    def wrapper():
        print('[LOG] 函数开始执行')
        func()
        print('[LOG] 函数执行完毕')
    return wrapper

def say_hello():
    print("Hello World")
def say_bye():
    print("Goodbye")

say_hello=log_decorator(say_hello)
say_bye=log_decorator(say_bye)
say_hello()
say_bye()

# TODO: 手动装饰：say_hello = log_decorator(say_hello)
# TODO: 用 @log_decorator 语法糖重写，效果一样但更优雅
@log_decorator
def say_hello():
    print("Hello World")

@log_decorator
def say_bye():
    print("Goodbye")

say_hello()
say_bye()

# ============================================================
# 第2节：装饰器进阶——带参数的函数（15min）
# ============================================================

# TODO: 改造 log_decorator，wrapper 用 *args, **kwargs 接收任意参数
# TODO: 打印 func.__name__、参数、返回值
# TODO: 别忘了 return result！




# TODO: 用改造后的装饰器装饰 add(a, b) 和 greet(name, greeting="你好")
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用{func.__name__},参数：{args},{kwargs}")
        result=func(*args, **kwargs)
        print(f"[LOG] {func.__name__}返回:{result}")
        return result
    return wrapper

@log_decorator
def add(a,b):
    return a+b

@log_decorator
def greet(name,greeting="你好"):
    return f"{greeting}, {name}"

print(add(3,5))
print(greet("张三",greeting="早上好"))

# TODO: 写一个 timer 装饰器——用 time.time() 测量函数执行时间
# TODO: 装饰 slow_function()，观察耗时
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时：{end-start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    total = 0
    for i in range(10000000):
        total += i
    return total

result = slow_function()
print(f"结果：{result}")

# ============================================================
# 第3节：@property 装饰器（15min）
# ============================================================

# TODO: 定义 Student 类，_score 存储分数
# TODO: @property 实现 score getter
# TODO: @score.setter 实现 score setter，验证 0-100 范围
# TODO: @property 实现 grade 计算属性（根据分数返回等级）


# TODO: 测试：像属性一样读写 score，访问 grade
# TODO: 测试设置非法分数（如150），看是否触发 ValueError
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def get_grade(self):
        if self.score>=90:
            return "优秀"
        elif self.score>=80:
            return "良好"
        elif self.score>=70:
            return "中等"
        elif self.score>=60:
            return "及格"
        else:
            return "不及格"

s=Student("张三",85)
print(s.get_grade())
print(s.score)

class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not 0<=value<=100:
            raise ValueError("分数必须在 0-100 之间")
        self._score=value

    @property
    def grade(self):
        if self._score>=90:
            return "优秀"
        elif self._score>=80:
            return "良好"
        elif self._score>=70:
            return "中等"
        elif self._score>=60:
            return "及格"
        else:
            return "不及格"

s=Student("张三",85)
print(s.score)
print(s.grade)

s.score=92
print(s.grade)
# ============================================================
# 第4节：组合 vs 继承（10min）
# ============================================================

# TODO: 定义 Engine 类：__init__(horsepower), start(), stop()
# TODO: 定义 Tire 类：__init__(size), info()
# TODO: 定义 Car 类：__init__ 里 self.engine = Engine(...)（组合！）
#        Car 不是 Engine，Car 有一个 Engine
# TODO: Car 的 start/stop 委托给 self.engine


# TODO: 创建 Car 实例，测试 car_info()、start()、stop()
class Engine:
    def start(self):
        return "引擎启动"

class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
    def start(self):
        return f"{self.horsepower}马力引擎启动，轰轰轰~~~"
    def stop(self):
        return "引擎熄火"

class Tire:
    def __init__(self,size):
        self.size=size
    def info(self):
        return f"{self.size}"

class Car:
    def __init__(self,brand,engine_hp,tire_size):
        self.brand=brand
        self.engine=Engine(engine_hp)
        self.tires=[Tire(tire_size) for _ in range(4)]
    def start(self):
        return f"{self.brand}:{self.engine.start()}"
    def stop(self):
        return f"{self.brand}:{self.engine.stop()}"
    def car_info(self):
        return f"{self.brand},{self.engine.horsepower}马力,{self.tires[0].size}寸轮胎"

my_car=Car("小米SU7",673,19)
print(my_car.car_info())
print(my_car.start())
print(my_car.stop())

# ============================================================
# 综合练习
# ============================================================

# TODO 练习1：写一个 @retry(times=3) 装饰器
#       装饰器带参数 → 需要三层嵌套
#       被装饰函数抛异常就重试，最多 times 次
#       提示：用 @functools.wraps(func) 保留原函数信息


# TODO 练习2：Temperature 类（用 @property）
#       celsius 属性：可读写，setter 验证 ≥ -273.15（绝对零度）
#       fahrenheit 属性：只读计算属性，F = C × 9/5 + 32


# TODO 练习3：游戏角色系统（用组合）
#       Weapon 类：name, damage, attack()
#       Armor 类：name, defense, block()
#       Character 类：组合 Weapon + Armor
#           方法：attack(target)、defend(damage)、change_weapon()、change_armor()
#       创建战士和哥布林，模拟战斗

