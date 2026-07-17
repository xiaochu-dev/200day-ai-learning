# Day 5（2026.07.16）— 装饰器与组合

> Phase 1 Week 2：类/继承/装饰器/生成器/import机制
> 今日主题：**装饰器、@property、组合 vs 继承**

---

## 英语 30min

| 时间段 | 任务 | 内容 |
|--------|------|------|
| 早/睡前 | **背单词 15min** | 下面30个六级高频词——看英文想中文意思（**不拼写**），记不住的拿笔写两遍 |
| 早/睡前 | **听力 15min** | 去 [VOA常速英语](https://www.51voa.com/) 找一篇1-2分钟的新闻，听3遍：第1遍盲听理解大意，第2遍看原文跟读，第3遍再盲听检查自己能听懂多少 |

#### 今日30词（Day 5 六级高频词 #121-150）

> **Day 1-4 复习**：先花4分钟快速过一遍前四天的120个词（遮中文说意思），忘记的标记一下。
> **学习方式**：先整体看一遍，然后用手遮住中文列，看英文说中文意思。说不出的做标记，第二轮重点复习标记词。
> **过关标准**：遮住中文，30个里至少 **24个能说出正确意思（80%）**。达不到就标记错词、复习、再测，直到通过。

| # | 英文 | 中文 |
|---|------|------|
| 1 | **assemble** | v. 集合；组装 |
| 2 | **assess** | v. 评估；评定 |
| 3 | **associate** | v. 联系；关联 n. 伙伴；同事 |
| 4 | **assume** | v. 假设；承担（责任） |
| 5 | **atmosphere** | n. 气氛；氛围；大气层 |
| 6 | **attach** | v. 附上；连接；依恋 |
| 7 | **attain** | v. 达到；获得 |
| 8 | **attribute** | v. 归因于 n. 属性；特质 |
| 9 | **authority** | n. 权威；当局；权力 |
| 10 | **available** | a. 可用的；有空的 |
| 11 | **barrier** | n. 障碍；屏障 |
| 12 | **behalf** | n. 代表（on behalf of） |
| 13 | **behave** | v. 行为；表现 |
| 14 | **benefit** | n. 利益；好处 v. 受益 |
| 15 | **bond** | n. 纽带；债券；结合 |
| 16 | **bonus** | n. 奖金；额外收获 |
| 17 | **boom** | n./v. 繁荣；激增；轰鸣 |
| 18 | **boundary** | n. 边界；界限 |
| 19 | **brief** | a. 简短的 n. 摘要 v. 简要介绍 |
| 20 | **budget** | n. 预算 v. 做预算 |
| 21 | **bulk** | n. 大量；大块；主体 |
| 22 | **burden** | n. 负担 v. 使负重 |
| 23 | **campaign** | n. 运动（政治/广告）；战役 |
| 24 | **capable** | a. 有能力的 |
| 25 | **capacity** | n. 容量；能力；职位 |
| 26 | **capture** | v. 捕获；占领；吸引（注意力） |
| 27 | **career** | n. 职业；生涯 |
| 28 | **category** | n. 类别；范畴 |
| 29 | **cease** | v. 停止；终止 |
| 30 | **challenge** | n./v. 挑战；质疑 |

#### 自测记录

- [x] 第1轮：答对 18 / 30（≥24 过关）
- [x] 补测 第2轮：答对 8 / 12
- [x] 补测 第3轮：答对 4 / 4 ✅ 过关

---

## AI 开发 90min

### 今日概述

Day 4 学了继承。今天学两个新概念：**装饰器**（给函数加额外功能）和**组合**（比继承更灵活的代码复用方式）。

> **核心思想**：
> - 装饰器 = 给函数"穿衣服"，不改原函数，加新功能
> - 组合 = "有一个（has-a）"关系——Car 有一个 Engine，而不是 Car 继承 Engine

---

### 第一部分：知识点学习（60min）

按顺序敲完以下代码，**全部手打，不要复制粘贴**。每个小节跑通再进入下一节。

#### 1. 装饰器入门（20min）

```python
# === 什么是装饰器？===
# 装饰器就是一个函数，它接收一个函数，返回一个新函数
# 用来在不修改原函数的情况下，添加额外功能

# === 先理解：函数也是对象 ===
def greet():
    return "Hello!"

print(greet)        # <function greet at 0x...> —— 函数本身是一个对象
print(greet())      # "Hello!" —— 调用函数

f = greet           # 把函数赋值给变量
print(f())          # "Hello!" —— 通过变量调用


# === 场景：想在函数执行前后打印日志 ===
# 不用装饰器的话，要这样写（重复代码多）：
def say_hello():
    print("[LOG] 函数开始执行")
    print("Hello World")
    print("[LOG] 函数执行完毕")

def say_bye():
    print("[LOG] 函数开始执行")
    print("Goodbye")
    print("[LOG] 函数执行完毕")

say_hello()
say_bye()
# 每个函数都要重复写 LOG，太麻烦了！


# === 用装饰器解决 ===
def log_decorator(func):
    """装饰器：给函数加日志"""
    def wrapper():
        print("[LOG] 函数开始执行")   # 执行前
        func()                        # 调用原函数
        print("[LOG] 函数执行完毕")   # 执行后
    return wrapper


def say_hello():
    print("Hello World")

def say_bye():
    print("Goodbye")

# 用装饰器"包装"函数
say_hello = log_decorator(say_hello)
say_bye = log_decorator(say_bye)

say_hello()
# [LOG] 函数开始执行
# Hello World
# [LOG] 函数执行完毕

say_bye()
# [LOG] 函数开始执行
# Goodbye
# [LOG] 函数执行完毕


# === @语法糖：更优雅的写法 ===
# 上面的 say_hello = log_decorator(say_hello) 可以写成：

@log_decorator      # 等价于 say_hello = log_decorator(say_hello)
def say_hello():
    print("Hello World")

@log_decorator
def say_bye():
    print("Goodbye")

# 效果完全一样，但 @ 语法更清晰
say_hello()
say_bye()
```

#### 2. 装饰器进阶：带参数的函数（15min）

```python
# === 问题：如果原函数有参数怎么办？===

def log_decorator(func):
    def wrapper(*args, **kwargs):           # *args, **kwargs 接收任意参数
        print(f"[LOG] 调用 {func.__name__}，参数：{args}, {kwargs}")
        result = func(*args, **kwargs)       # 原封不动传给原函数
        print(f"[LOG] {func.__name__} 返回：{result}")
        return result                        # 别忘了返回结果！
    return wrapper


@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"

print(add(3, 5))
# [LOG] 调用 add，参数：(3, 5), {}
# [LOG] add 返回：8
# 8

print(greet("张三", greeting="早上好"))
# [LOG] 调用 greet，参数：('张三',), {'greeting': '早上好'}
# [LOG] greet 返回：早上好，张三！
# 早上好，张三！


# === 计时装饰器：一个实用的例子 ===
import time

def timer(func):
    """测量函数执行时间"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时：{end - start:.4f} 秒")
        return result
    return wrapper


@timer
def slow_function():
    """模拟耗时操作"""
    total = 0
    for i in range(10_000_000):
        total += i
    return total

result = slow_function()
print(f"结果：{result}")
# slow_function 耗时：0.xxxx 秒
# 结果：49999995000000
```

#### 3. @property 装饰器（15min）

```python
# === @property：让方法像属性一样访问 ===

# 不用 @property 时，这样访问属性：
class Student:
    def __init__(self, name, score):
        self.name = name
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

s = Student("张三", 85)
print(s.get_grade())   # "良好" —— 要加括号，是个方法调用
print(s.score)          # 85 —— 属性直接访问，不需要括号

# 问题：get_grade 本质上是"计算属性"，应该像属性一样访问
# 用 @property 解决：


class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score   # 用 _score 存储，避免和属性名冲突

    @property
    def score(self):
        """获取分数"""
        return self._score

    @score.setter
    def score(self, value):
        """设置分数，加验证"""
        if not 0 <= value <= 100:
            raise ValueError("分数必须在 0-100 之间！")
        self._score = value

    @property
    def grade(self):
        """等级——计算属性，像属性一样访问"""
        if self._score >= 90:
            return "优秀"
        elif self._score >= 80:
            return "良好"
        elif self._score >= 70:
            return "中等"
        elif self._score >= 60:
            return "及格"
        else:
            return "不及格"


s = Student("张三", 85)
print(s.score)    # 85 —— 不用加括号！像属性一样
print(s.grade)    # "良好" —— 计算属性，也不是方法调用

s.score = 92      # 调用 setter，自动验证
print(s.grade)    # "优秀"

# s.score = 150   # ❌ ValueError: 分数必须在 0-100 之间！


# === @property 总结 ===
# @property        → getter，读属性时调用
# @xxx.setter      → setter，写属性时调用
# @xxx.deleter     → deleter，del 属性时调用（用得少）

# 好处：
# 1. 方法变属性，代码更优雅
# 2. 可以在 setter 里加数据验证
# 3. 可以先当普通属性用，后面需要验证时改成 property，不影响外部调用
```

#### 4. 组合 vs 继承（10min）

```python
# === 继承 vs 组合：什么时候用哪个？===

# Day 4 说过：继承 = "是一个（is-a）"关系
# 今天学：组合 = "有一个（has-a）"关系


# ❌ 错误示范：用继承表达"有一个"关系
class Engine:
    def start(self):
        return "引擎启动"

# class Car(Engine):    # ❌ Car 是一个 Engine？不对！
#     pass              #    Car 有一个 Engine，不是 Engine


# ✅ 正确：用组合
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"{self.horsepower}马力引擎启动，轰轰轰~~~"

    def stop(self):
        return "引擎熄火"


class Tire:
    def __init__(self, size):
        self.size = size

    def info(self):
        return f"{self.size}寸轮胎"


class Car:
    """汽车——由引擎、轮胎组合而成"""
    def __init__(self, brand, engine_hp, tire_size):
        self.brand = brand
        self.engine = Engine(engine_hp)     # Car 有一个 Engine（组合！）
        self.tires = [Tire(tire_size) for _ in range(4)]  # Car 有4个轮胎

    def start(self):
        return f"{self.brand}：{self.engine.start()}"

    def stop(self):
        return f"{self.brand}：{self.engine.stop()}"

    def car_info(self):
        return f"{self.brand}，{self.engine.horsepower}马力，{self.tires[0].size}寸轮胎"


# 使用
my_car = Car("小米SU7", 673, 19)
print(my_car.car_info())   # 小米SU7，673马力，19寸轮胎
print(my_car.start())      # 小米SU7：673马力引擎启动，轰轰轰~~~
print(my_car.stop())       # 小米SU7：引擎熄火


# === 判断口诀 ===
# is-a（是一个）→ 继承
#   ✅ Dog is an Animal        → class Dog(Animal)
#   ✅ Monitor is a Student    → class Monitor(Student)

# has-a（有一个）→ 组合
#   ✅ Car has an Engine       → self.engine = Engine()
#   ✅ Student has a Phone     → self.phone = Phone()

# 一句话：组合比继承更灵活，不确定的时候优先用组合
```

---

### 第二部分：综合练习（做完才看答案）

> **练习1：写一个重试装饰器**
>
> 写一个 `@retry(times=3)` 装饰器：被装饰的函数如果抛出异常，自动重试，最多重试 `times` 次。全部失败才报错。
>
> 提示：装饰器本身也能带参数——需要再包一层函数。

> **练习2：Temperature 类**
>
> 用 `@property` 实现一个温度类：
> - `celsius` 属性：摄氏温度（可读写）
> - `fahrenheit` 属性：华氏温度（计算属性，只读）
> - 公式：F = C × 9/5 + 32
> - 设置 celsius 时验证不能低于 -273.15（绝对零度）

> **练习3：游戏角色系统（组合）**
>
> 用组合模式设计一个游戏角色系统：
> ```
> Weapon（武器类）
> ├── 属性：name, damage
> └── 方法：attack() → "用{name}造成{damage}点伤害"
>
> Armor（防具类）
> ├── 属性：name, defense
> └── 方法：block() → "{name}抵挡了{defense}点伤害"
>
> Character（角色类）——组合 Weapon 和 Armor
> ├── 属性：name, weapon, armor
> └── 方法：attack()、defend()、change_weapon()、change_armor()
> ```
> 要求：角色可以换武器、换防具，攻击和防御行为随之改变。

<details>
<summary>参考答案（做完再看）</summary>

```python
# ========== 练习1：重试装饰器 ==========

import functools

def retry(times=3):
    """装饰器工厂：返回一个装饰器"""
    def decorator(func):
        @functools.wraps(func)     # 保留原函数的 __name__ 和 __doc__
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"[重试] {func.__name__} 第{attempt}次失败：{e}")
            raise last_error   # 全部失败，抛出最后一次的错误
        return wrapper
    return decorator


@retry(times=3)
def unstable_network():
    """模拟不稳定的网络请求"""
    import random
    if random.random() < 0.7:      # 70% 概率失败
        raise ConnectionError("网络连接超时！")
    return "数据获取成功！"


# 测试（多跑几次看看重试效果）
for i in range(5):
    try:
        print(unstable_network())
    except ConnectionError as e:
        print(f"最终失败：{e}")
    print("---")


# ========== 练习2：Temperature 类 ==========

class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius   # 会调用 setter 验证

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"温度 {value}°C 低于绝对零度（-273.15°C）！")
        self._celsius = value

    @property
    def fahrenheit(self):
        """华氏温度 = 摄氏 × 9/5 + 32"""
        return self.celsius * 9 / 5 + 32

    def __str__(self):
        return f"{self.celsius:.2f}°C / {self.fahrenheit:.2f}°F"


# 测试
t = Temperature(25)
print(t)                      # 25.00°C / 77.00°F
t.celsius = 100
print(t)                      # 100.00°C / 212.00°F
t.celsius = -40
print(t)                      # -40.00°C / -40.00°F
# t.celsius = -300            # ❌ ValueError!


# ========== 练习3：游戏角色系统（组合）==========

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return f"用{self.name}造成{self.damage}点伤害"

    def __str__(self):
        return f"{self.name}（攻击力{self.damage}）"


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def block(self):
        return f"{self.name}抵挡了{self.defense}点伤害"

    def __str__(self):
        return f"{self.name}（防御力{self.defense}）"


class Character:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon     # 组合：角色有一个武器
        self.armor = armor       # 组合：角色有一个防具
        self.hp = 100

    def attack(self, target):
        """攻击另一个角色"""
        msg = f"{self.name} {self.weapon.attack()}"
        target.defend(self.weapon.damage)
        return msg

    def defend(self, damage):
        """受到攻击"""
        actual_damage = max(0, damage - self.armor.defense)
        self.hp -= actual_damage
        print(f"  {self.name} {self.armor.block()}，实际受伤{actual_damage}点，剩余HP：{self.hp}")

    def change_weapon(self, new_weapon):
        old = self.weapon
        self.weapon = new_weapon
        return f"{self.name}更换武器：{old} → {new_weapon}"

    def change_armor(self, new_armor):
        old = self.armor
        self.armor = new_armor
        return f"{self.name}更换防具：{old} → {new_armor}"

    def __str__(self):
        return f"{self.name}（HP:{self.hp}，武器：{self.weapon}，防具：{self.armor}）"


# 测试
if __name__ == "__main__":
    sword = Weapon("铁剑", 30)
    axe = Weapon("战斧", 50)
    leather = Armor("皮甲", 10)
    plate = Armor("板甲", 25)

    warrior = Character("战士", sword, leather)
    enemy = Character("哥布林", Weapon("木棍", 15), Armor("布衣", 3))

    print(warrior)
    print(enemy)
    print()

    print(warrior.attack(enemy))
    print()

    # 战士换装备
    print(warrior.change_weapon(axe))
    print(warrior.change_armor(plate))
    print()

    print(warrior.attack(enemy))
```

</details>

---

### 第三部分：笔记 + GitHub 提交（10min）

1. 把今天写的代码保存为 `Day05_decorators_composition.py`
2. 提交并推送：

```bash
cd E:\Users\MyFiles\Desktop\200day
git add Day5
git commit -m "Day05: 装饰器、@property、组合vs继承"
git push
```

---

### 今日要记住的要点

| 要点 | 为什么重要 |
|------|-----------|
| `@decorator` | 不改原函数加功能——日志、计时、重试、权限检查等场景 |
| `*args, **kwargs` | 装饰器用它们接收任意参数，通用性强 |
| `@property` | 方法变属性，setter 里加验证——Python 风格的 getter/setter |
| 组合 > 继承 | is-a 用继承，has-a 用组合。不确定时选组合 |
| `@functools.wraps` | 写装饰器时加这行，保留原函数的 `__name__` 和文档 |

---

## 今日打卡清单

- [ ] 30个六级单词自测 ≥ 24分 + 花4分钟复习Day 1-4单词
- [ ] 精听1篇 VOA 常速新闻
- [ ] 手敲了装饰器入门、@property、组合的所有代码
- [ ] 独立完成了重试装饰器 + Temperature + 游戏角色三个练习
- [ ] 代码 push 到了 GitHub

---

## 今日提示

装饰器看着花哨，本质就一句话：**一个函数，接收函数，返回新函数**。

把它想成"给函数穿外套"——外套（装饰器）可以在函数运行前后做任何事，但不改变函数本身。

初学最容易忘的两件事：
1. `wrapper` 里别忘了 `return result`
2. 带参数的装饰器需要三层嵌套：`def 装饰器工厂(参数): def 装饰器(func): def wrapper(...): ... return wrapper; return 装饰器`

**@functools.wraps 一定要加！** 否则被装饰的函数会丢失自己的名字和文档字符串，debug 的时候哭都来不及。

完成后告诉我，帮你准备 Day 6 的内容。加油 💪
