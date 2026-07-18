"""
Day 6 — 生成器与模块
主题：迭代器、yield 生成器、生成器表达式、模块与 import
按顺序手打以下代码，每个小节跑通再进入下一节。
参考答案在 Day06_任务安排.md 里。
"""


# ============================================================
# 第1节：迭代器——for 循环的本质（10min）
# ============================================================

# TODO: 理解 iter() 和 next()，用它们手动遍历列表 [1, 2, 3]
# TODO: 用 iter("abc") 创建迭代器，next 两次，体会"一次性的"

nums=[1,2,3]
for n in nums:
    print(n)

it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

it = iter("abc")
print(next(it))
print(next(it))



# ============================================================
# 第2节：生成器函数——yield（20min）
# ============================================================

# TODO: 写 count_up_list(n)：用列表 return 所有数（对比用）
# TODO: 写 count_up_gen(n)：用 yield 逐个产出
# TODO: 用 next() 取3个数，再用 for 循环遍历
# TODO: 用 sys.getsizeof 对比 100万个数的列表 vs 生成器的内存


# TODO: 写 demo() 生成器：yield 1，打印一句话，再 yield 2
#       用 next 两次，体会"暂停后继续"


# TODO: 写 read_lines(filename)：用 yield 逐行产出文件内容（去换行符）
#       提示：文件对象本身就是迭代器，可以逐行 for

def count_up_list(n):
    result = []
    for i in range(1,n+1):
        result.append(i)
    return result

print(count_up_list(5))

def count_up_gen(n):
    for i in range(1,n+1):
        yield i

g=count_up_gen(5)
print(g)
print(next(g))
print(next(g))
print(next(g))

for i in count_up_gen(5):
    print(i,end=" ")
print()

import sys
big_list = [i for i in range(1000000)]
big_gen=(i for i in range(1000000))
print(f"列表占内存:{sys.getsizeof(big_list):,}字节")
print(f"生成器占内存：{sys.getsizeof(big_gen):,}字节")

def demo():
    print("开始")
    yield 1
    print("第一次暂停后继续")
    yield 2
    print("第二次暂停后继续，马上结束")

g=demo()
next(g)
next(g)

def read_lines(filename):
    with open(filename,encoding="wtf-8") as f:
        for line in f:
            yield line.strip()
# ============================================================
# 第3节：生成器表达式（10min）
# ============================================================

# TODO: 把 [x**2 for x in range(10)] 的 [] 改成 ()，看看返回值是什么
# TODO: 用 sum(x**2 for x in range(1000000)) 省掉中间列表
# TODO: 用 max(x**2 for x in range(1, 101) if x % 7 == 0) 找最大平方数

squares_list = [x**2 for x in range(10)]
squares_gen = (x**2 for x in range(10))

print(squares_list)
print(squares_gen)
print(list(squares_gen))

total = sum(x**2 for x in range(1000000))
print(total)
print(max(x**2 for x in range(1,101) if x % 7 == 0))

# ============================================================
# 第4节：模块与 import 机制（20min）
# ============================================================

# TODO: import math → 用 math.sqrt(16) 和 math.pi
# TODO: from math import sqrt, pi → 直接用 sqrt(16)
# TODO: import random as rd → 用 rd.randint(1, 10)


# TODO: 写 if __name__ == "__main__": 打印一句话
#       理解：直接运行打印，被 import 时不打印

import math
print(math.sqrt(16))
print(math.pi)

from math import sqrt,pi
print(sqrt(16))

import random as rd
print(rd.randint(1,100))

if __name__ == '__main__':
    print("直接运行才会打印这句，被 import 时不会")

import os
import sys
import json
import datetime
import random
import time
# ============================================================
# 练习1：斐波那契生成器
# ============================================================

# TODO: 写 fib(n) —— 产出斐波那契数列前 n 项（1, 1, 2, 3, 5, 8...）
#       提示：a, b = 1, 1 然后 a, b = b, a+b


# TODO: 写 fib_infinite() —— while True + yield，无限产出
# TODO: 用计数+break 取前10项
# TODO: from itertools import islice → 用 islice 取前10项


# ============================================================
# 练习2：日志分析生成器管道
# ============================================================

# TODO: 先跑"造数据"代码生成 server.log（见任务安排.md）
# TODO: 写 read_log(filename) —— 逐行 yield line.strip()
# TODO: 写 filter_errors(lines) —— 只 yield 含 "ERROR" 的行
# TODO: 组装管道：errors = filter_errors(read_log("server.log"))
# TODO: 遍历 errors，统计总数 + 收集前5条（一次循环做完！生成器只能遍历一次）


