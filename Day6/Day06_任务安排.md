# Day 6（2026.07.17）— 生成器与模块

> Phase 1 Week 2：类/继承/装饰器/生成器/import机制
> 今日主题：**迭代器、生成器（yield）、模块与import机制**

---

## 英语 30min

| 时间段 | 任务 | 内容 |
|--------|------|------|
| 早/睡前 | **背单词 15min** | 下面30个六级高频词——看英文想中文意思（**不拼写**），记不住的拿笔写两遍 |
| 早/睡前 | **听力 15min** | 去 [VOA常速英语](https://www.51voa.com/) 找一篇1-2分钟的新闻，听3遍：第1遍盲听理解大意，第2遍看原文跟读，第3遍再盲听检查自己能听懂多少 |

#### 今日30词（Day 6 六级高频词 #151-180）

> **Day 1-5 复习**：先花5分钟快速过一遍前五天的150个词（遮中文说意思），忘记的标记一下。昨天错过的 attain/cease/attribute/bulk/burden/bonus 这类词重点看。
> **学习方式**：先整体看一遍，然后用手遮住中文列，看英文说中文意思。说不出的做标记，第二轮重点复习标记词。
> **过关标准**：遮住中文，30个里至少 **24个能说出正确意思（80%）**。达不到就标记错词、复习、再测，直到通过。

| # | 英文 | 中文 |
|---|------|------|
| 1 | **chamber** | n. 房间；会议厅；腔 |
| 2 | **chaos** | n. 混乱；无序 |
| 3 | **characteristic** | n. 特征 a. 典型的；独特的 |
| 4 | **charge** | v./n. 收费；充电；指控；负责（in charge of） |
| 5 | **charity** | n. 慈善；慈善机构 |
| 6 | **chart** | n. 图表 v. 记录；绘制 |
| 7 | **chase** | v./n. 追逐；追求 |
| 8 | **cheat** | v. 欺骗；作弊 |
| 9 | **chemical** | a. 化学的 n. 化学物质 |
| 10 | **cherish** | v. 珍惜；怀有（希望） |
| 11 | **chief** | a. 主要的；首席的 n. 首领 |
| 12 | **circulate** | v. 循环；流通；传播 |
| 13 | **circumstance** | n. 环境；情况 |
| 14 | **cite** | v. 引用；举例 |
| 15 | **civil** | a. 公民的；民事的；文明的 |
| 16 | **claim** | v./n. 声称；索取；夺去（生命） |
| 17 | **clarify** | v. 澄清；阐明 |
| 18 | **classify** | v. 分类 |
| 19 | **cling** | v. 紧抓；依附；坚持（cling to） |
| 20 | **clue** | n. 线索；提示 |
| 21 | **coincide** | v. 同时发生；相符 |
| 22 | **collaborate** | v. 合作 |
| 23 | **collapse** | v./n. 倒塌；崩溃 |
| 24 | **colleague** | n. 同事 |
| 25 | **collide** | v. 碰撞；冲突 |
| 26 | **combat** | n./v. 战斗；对抗 |
| 27 | **combine** | v. 结合；联合 |
| 28 | **commence** | v. 开始 |
| 29 | **comment** | n./v. 评论；意见 |
| 30 | **commit** | v. 犯（罪/错）；承诺；投入 |

#### 自测记录

- [ ] 第1轮：答对 __ / 30（≥24 过关）
- [ ] 补测（如需要）：

---

## AI 开发 90min

### 今日概述

Day 5 学了装饰器（给函数加功能）。今天学 Week 2 最后两个知识点：

- **生成器**：一种"用一个取一个"的省内存迭代方式——处理大数据的必备技能，AI 里的流式输出（打字机效果）底层就是它
- **模块与 import**：把代码拆到多个文件里——明天写学生管理系统就要用，以后所有项目都是多文件的

> **核心思想**：
> - 生成器 = "点菜现做"，列表 = "全部做好摆桌上"。数据量大时，现做省地方
> - 模块 = 把一个大 py 文件拆成几个小文件，各管各的，用 import 组装

---

### 第一部分：知识点学习（60min）

按顺序敲完以下代码，**全部手打，不要复制粘贴**。每个小节跑通再进入下一节。

#### 1. 迭代器：for 循环的本质（10min）

```python
# === for 循环背后发生了什么？===

nums = [1, 2, 3]

# 你平时写的：
for n in nums:
    print(n)

# 实际上 Python 在背后做的是：
it = iter(nums)      # 1. 拿到迭代器
print(next(it))      # 1  —— 2. 不断调用 next() 取下一个
print(next(it))      # 2
print(next(it))      # 3
# print(next(it))    # ❌ StopIteration —— 3. 取完了就报这个错，for 循环捕获它并结束

# === 两个概念 ===
# 可迭代对象（Iterable）：能被 for 遍历的东西——list、str、dict、文件对象...
# 迭代器（Iterator）：  记住"取到哪了"的对象，只能往前走，不能回头

it = iter("abc")
print(next(it))   # 'a'
print(next(it))   # 'b'
# 迭代器是一次性的！取完就空了，想重来要重新 iter()
```

#### 2. 生成器函数：yield（20min）

```python
# === 问题：想要一个"能产生一堆值"的函数 ===

# 方法1：用列表 return（你已经会的）
def count_up_list(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result

print(count_up_list(5))    # [1, 2, 3, 4, 5]
# 问题：如果 n 是 1 亿，这个列表要占几个 GB 内存！


# 方法2：用生成器 yield（今天学的）
def count_up_gen(n):
    for i in range(1, n + 1):
        yield i            # yield = "产出一个值，然后暂停在这里"

g = count_up_gen(5)
print(g)                   # <generator object ...> —— 调用函数不执行，返回生成器对象
print(next(g))             # 1 —— 执行到第一个 yield，暂停
print(next(g))             # 2 —— 从上次暂停处继续，到下一个 yield
print(next(g))             # 3

# 生成器就是迭代器，可以直接 for：
for i in count_up_gen(5):
    print(i, end=" ")      # 1 2 3 4 5
print()


# === 关键区别：懒惰求值 ===
# count_up_list(100000000)  → 立刻生成1亿个数的列表，内存爆炸
# count_up_gen(100000000)   → 瞬间返回，一个数都没生成；用一个才算一个，内存只占一个数

# 用 sys.getsizeof 看内存差距：
import sys
big_list = [i for i in range(1000000)]
big_gen = (i for i in range(1000000))
print(f"列表占内存：{sys.getsizeof(big_list):,} 字节")   # 约 8,000,000+
print(f"生成器占内存：{sys.getsizeof(big_gen):,} 字节")  # 约 200（不管多少数据都这么大！）


# === yield 和 return 的区别 ===
# return：函数结束，返回一个值
# yield： 函数暂停，产出一个值，下次从暂停处继续
# 一个函数里只要出现 yield，它就是生成器函数

def demo():
    print("开始")
    yield 1
    print("第一次暂停后继续")
    yield 2
    print("第二次暂停后继续，马上结束")

g = demo()
next(g)     # 打印"开始"，产出 1
next(g)     # 打印"第一次暂停后继续"，产出 2
# next(g)   # 打印"第二次...结束"，然后 StopIteration


# === 实用场景：逐行处理大文件 ===
# 文件对象本身就是生成器思想的应用——不会把整个文件读进内存
def read_lines(filename):
    """逐行产出文件内容（去掉换行符）"""
    with open(filename, encoding="utf-8") as f:
        for line in f:          # 文件对象天生支持逐行迭代，省内存
            yield line.strip()

# 就算文件有 10GB，内存也只占一行的大小
```

#### 3. 生成器表达式（10min）

```python
# === 长得像列表推导式，把 [] 换成 () ===

squares_list = [x ** 2 for x in range(10)]    # 列表推导式：立刻算完
squares_gen = (x ** 2 for x in range(10))     # 生成器表达式：用到才算

print(squares_list)         # [0, 1, 4, 9, ...]
print(squares_gen)          # <generator object ...>
print(list(squares_gen))    # 想看全部就转 list（数据量小的时候）


# === 最常见用法：喂给 sum / max / min，不用中间列表 ===
total = sum(x ** 2 for x in range(1000000))   # 传给函数时括号都能省
print(total)

# 找出 1~100 中能被 7 整除的数的最大平方
print(max(x ** 2 for x in range(1, 101) if x % 7 == 0))   # 9604 (98²)


# === 什么时候用哪个？===
# 需要反复用、要取长度、要切片      → 列表推导式
# 只遍历一遍（尤其配合sum/max/for） → 生成器表达式，省内存
```

#### 4. 模块与 import 机制（20min）

```python
# === 什么是模块？===
# 一个 .py 文件就是一个模块。import 就是"把别的文件里的代码拿来用"

# --- 用法1：import 整个模块 ---
import math
print(math.sqrt(16))        # 4.0 —— 用 模块名.函数名 访问
print(math.pi)              # 3.141592653589793

# --- 用法2：只导入需要的东西 ---
from math import sqrt, pi
print(sqrt(16))             # 直接用，不用加 math. 前缀

# --- 用法3：起别名（约定俗成的缩写） ---
import random as rd
print(rd.randint(1, 10))
# 以后学数据处理会天天见：import numpy as np / import pandas as pd

# --- ❌ 不推荐：from math import * ---
# 把所有东西倒进来，容易和自己的变量重名，出了bug都不知道哪来的


# === 自定义模块：自己写的 py 文件也能 import ===
# 假设同一文件夹下有个 mytools.py，内容是：
#     def double(x):
#         return x * 2
#     PI = 3.14
#
# 在另一个文件里就可以：
#     import mytools
#     print(mytools.double(5))     # 10
#     print(mytools.PI)            # 3.14
#
# 或者：
#     from mytools import double


# === __name__ == "__main__" 的秘密 ===
# 每个模块都有一个内置变量 __name__：
#   - 直接运行这个文件时，__name__ 的值是 "__main__"
#   - 被别人 import 时，  __name__ 的值是模块名（文件名）

# 所以这个写法的意思是"只有直接运行我时才执行"：
if __name__ == "__main__":
    print("直接运行才会打印这句，被 import 时不会")

# 用途：模块里放测试代码。别人 import 你的工具函数时，
# 不会莫名其妙执行你的测试代码。这是 Python 的标准写法！


# === 常用标准库模块速览（不用背，混个脸熟）===
import os        # 文件/目录操作：os.listdir(), os.path.exists()
import sys       # 解释器相关：sys.argv 命令行参数
import json      # JSON读写：json.dumps(), json.loads() —— AI开发天天用
import datetime  # 日期时间
import random    # 随机数
import time      # time.sleep(), time.time()
```

---

### 第二部分：综合练习（做完才看答案）

> **练习1：斐波那契生成器**
>
> 写一个生成器函数 `fib(n)`：产出斐波那契数列的前 n 项（1, 1, 2, 3, 5, 8...）。
> 再写一个**无限版** `fib_infinite()`：没有 n，无限产出。然后想办法只取它的前10项打印出来（提示：for + 计数 + break，或者了解一下 `itertools.islice`）。

> **练习2：日志分析生成器**
>
> 先运行答案里的"造数据"代码生成 `server.log`（1000行模拟日志），然后**用生成器**实现：
> - `read_log(filename)`：逐行产出日志
> - `filter_errors(lines)`：接收上一个生成器，只产出包含 "ERROR" 的行
> - 统计 ERROR 行数，并打印前5条 ERROR
> - 要求全程不把文件整个读进内存（不许用 readlines()）
>
> 这种"生成器接生成器"的写法叫**管道（pipeline）**，数据处理的经典模式。

> **练习3：模块化改造（为明天做准备）**
>
> 把 Day 5 的游戏角色系统拆成 3 个文件（都放在 Day6 文件夹里）：
> ```
> weapons.py     → Weapon 类、Armor 类
> characters.py  → Character 类（from weapons import ...）
> game_main.py   → 创建角色、打一架（import characters）
> ```
> 要求：
> - weapons.py 和 characters.py 里各自用 `if __name__ == "__main__":` 放一段自己的测试代码
> - 只有运行 game_main.py 时才真正开打，运行/导入其他文件不会触发战斗

<details>
<summary>参考答案（做完再看）</summary>

```python
# ========== 练习1：斐波那契生成器 ==========

def fib(n):
    """产出斐波那契数列前 n 项"""
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b     # 同时更新，不需要临时变量

print(list(fib(10)))    # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def fib_infinite():
    """无限斐波那契生成器"""
    a, b = 1, 1
    while True:             # 无限循环也不怕——反正是暂停式执行
        yield a
        a, b = b, a + b

# 取前10项 方法1：手动计数
count = 0
for num in fib_infinite():
    print(num, end=" ")
    count += 1
    if count >= 10:
        break
print()

# 取前10项 方法2：itertools.islice（标准库的"生成器切片"）
from itertools import islice
print(list(islice(fib_infinite(), 10)))


# ========== 练习2：日志分析生成器 ==========

# --- 造数据（先跑这段，生成 server.log）---
import random

levels = ["INFO", "INFO", "INFO", "WARNING", "ERROR"]   # ERROR约占20%
messages = ["用户登录", "查询数据库", "连接超时", "内存不足", "请求成功"]

with open("server.log", "w", encoding="utf-8") as f:
    for i in range(1, 1001):
        level = random.choice(levels)
        msg = random.choice(messages)
        f.write(f"[2026-07-17 10:{i % 60:02d}:{i % 60:02d}] {level}: {msg}\n")

print("server.log 已生成")


# --- 生成器管道 ---
def read_log(filename):
    """逐行产出日志（生成器1）"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            yield line.strip()

def filter_errors(lines):
    """只产出 ERROR 行（生成器2，接收生成器1）"""
    for line in lines:
        if "ERROR" in line:
            yield line

# 组装管道：文件 → 逐行 → 过滤
errors = filter_errors(read_log("server.log"))

# 统计 + 打印前5条（注意：生成器只能遍历一次，所以一次循环里做完）
count = 0
first_five = []
for line in errors:
    count += 1
    if len(first_five) < 5:
        first_five.append(line)

print(f"ERROR 总数：{count}")
print("前5条 ERROR：")
for line in first_five:
    print(" ", line)


# ========== 练习3：模块化改造 ==========

# --- weapons.py ---
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


if __name__ == "__main__":
    # 只有直接运行 weapons.py 才会执行的测试
    w = Weapon("测试剑", 10)
    print("weapons.py 自测：", w.attack())


# --- characters.py ---
from weapons import Weapon, Armor


class Character:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.hp = 100

    def attack(self, target):
        msg = f"{self.name} {self.weapon.attack()}"
        target.defend(self.weapon.damage)
        return msg

    def defend(self, damage):
        actual = max(0, damage - self.armor.defense)
        self.hp -= actual
        print(f"  {self.name} {self.armor.block()}，实际受伤{actual}点，剩余HP：{self.hp}")

    def __str__(self):
        return f"{self.name}（HP:{self.hp}，武器：{self.weapon}，防具：{self.armor}）"


if __name__ == "__main__":
    # 只有直接运行 characters.py 才会执行的测试
    c = Character("测试角色", Weapon("木剑", 5), Armor("布衣", 2))
    print("characters.py 自测：", c)


# --- game_main.py ---
from weapons import Weapon, Armor
from characters import Character


def main():
    warrior = Character("战士", Weapon("铁剑", 30), Armor("皮甲", 10))
    goblin = Character("哥布林", Weapon("木棍", 15), Armor("布衣", 3))

    print(warrior)
    print(goblin)
    print()

    round_num = 1
    while warrior.hp > 0 and goblin.hp > 0:
        print(f"—— 第{round_num}回合 ——")
        print(warrior.attack(goblin))
        if goblin.hp <= 0:
            print(f"\n{goblin.name} 倒下了，{warrior.name} 获胜！")
            break
        print(goblin.attack(warrior))
        if warrior.hp <= 0:
            print(f"\n{warrior.name} 倒下了，{goblin.name} 获胜！")
            break
        round_num += 1


if __name__ == "__main__":
    main()
```

</details>

---

### 第三部分：笔记 + GitHub 提交（10min）

1. 练习1、2的代码保存为 `Day06_generators_modules.py`；练习3是 `weapons.py`、`characters.py`、`game_main.py` 三个文件
2. 提交并推送（现在配了443端口，开着代理也能推）：

```bash
cd E:\Users\MyFiles\Desktop\200day
git add Day6
git commit -m "Day06: 生成器、迭代器、模块与import"
git push
```

---

### 今日要记住的要点

| 要点 | 为什么重要 |
|------|-----------|
| `yield` | 函数暂停+产出值。有 yield 的函数就是生成器函数 |
| 惰性求值 | 生成器"用一个算一个"，处理大数据不爆内存 |
| 生成器只能遍历一次 | 取完就空，想重来要重新创建——最常踩的坑 |
| `(x for x in ...)` | 生成器表达式，配合 sum/max 不建中间列表 |
| `import` / `from...import` | 多文件项目的基础，明天就要用 |
| `if __name__ == "__main__":` | 模块被 import 时不执行测试代码——Python 标准写法 |

---

## 今日打卡清单

- [ ] 30个六级单词自测 ≥ 24分 + 花5分钟复习 Day 1-5 单词
- [ ] 精听1篇 VOA 常速新闻
- [ ] 手敲了迭代器、yield、生成器表达式、import 的所有代码
- [ ] 独立完成了斐波那契生成器 + 日志管道 + 模块化改造三个练习
- [ ] 代码 push 到了 GitHub

---

## 今日提示

生成器初看抽象，记住一个画面就懂了：**yield 是"暂停键"**。函数走到 yield 交出一个值就停在原地，下次 next() 再从停的地方继续走。

最容易踩的坑：**生成器是一次性的**。练习2里为什么统计数量和取前5条要在同一个循环里做？因为如果先 `count = sum(1 for _ in errors)` 数完，生成器就空了，再想取前5条什么都取不到。

模块部分概念不多，但 `if __name__ == "__main__":` 必须真正理解——分别直接运行 weapons.py 和运行 game_main.py，观察哪些打印出现了、哪些没出现，你就彻底懂了。

明天 Day 7 是 Week 2 收官：**综合运用类、继承、装饰器、生成器、模块，写一个多文件的学生管理系统**——今天的模块化练习就是给明天热身。加油 💪
