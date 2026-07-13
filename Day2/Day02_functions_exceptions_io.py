from encodings import utf_8


def greeting(name):
    """向指定的人打招呼"""
    return f'Hello, {name}!'
print(greeting('world'))
print(greeting.__doc__)

def power(base, exp=2):
    """计算base的exp次方，默认平方"""
    return base ** exp
print(power(3))
print(power(3, 3))

def add_item(item,lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
print(add_item(1))
print(add_item(2))

def describe_person(name,age,city="未知"):
    return f"{name},{age}岁,来自{city}"
print(describe_person("张三",20))
print(describe_person(age=22,name="李四"))
print(describe_person("王五",22,city="杭州"))

def my_sum(*args):
    total = 0
    for item in args:
        total += item
    return total
print(my_sum(1,2,3))
print(my_sum(1,2,3,4,5,6))

def build_profile(**kwargs):
    profile={}
    for key, value in kwargs.items():
        profile[key] = value
    return profile
user=build_profile(name="Alice",age=25,job="Engineer")
print(user)

def log_info(level,*args,**kwargs):
    print(f"[{level}]"," ".join(str(arg) for arg in args))
    if kwargs:
        print(" 附加信息：",kwargs)
log_info("INFO","用户","登录",ip="192.168.1.1",port=8080)

nums=[3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums=sorted(nums,key=lambda x:-x)
print(sorted_nums)

doubled=list(map(lambda x: x*2,nums))
evens_only=list(filter(lambda x: x%2==0,nums))
print("翻倍:",doubled)
print("偶数:",evens_only)

def safe_divice(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("错误，不能除以0")
        return None
    except TypeError:
        print("数据类型不正确")
        return None
    else:
        print(f"{a}/{b}={result}")
        return result
    finally:
        print(f"{a}/{b}执行完毕")
print(safe_divice(3,4))
print(safe_divice(3,0))
print()

def read_file_safe(filepath):
    try:
        with open(filepath, mode="r",encoding="utf_8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件不存在：{filepath}")
        return None
    except PermissionError:
        print(f"没有读取权限：{filepath}")
        return None
    except Exception as e:
        print(f"文件读写时发生未知错误：{e}")
        return None
content=read_file_safe("不存在的文件.txt")
print(content)

poem="""春眠不觉晓，
处处闻啼鸟。
夜来风雨声，
花落知多少。"""

with open("poem.txt","w",encoding="utf_8") as f:
    f.write(poem)
print("已写入poem.txt")

with open("poem.txt","r",encoding="utf_8") as f:
    content=f.read()
    print("文件内容：")
    print(content)

print("逐行读取：")
with open("poem.txt","r",encoding="utf_8") as f:
    for line_no, line in enumerate(f,1):
        print(f"第{line_no}行：{line.strip()}")

with open("poem.txt","r",encoding="utf_8") as f:
    lines=f.readlines()
    print(f"总共{len(lines)}行")

with open("poem.txt","a",encoding="utf_8") as f:
    f.write("\n---古诗一首---")
    print("已追加署名")

import csv
with open("students.csv","w",encoding="utf-8-sig",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["姓名","年龄","分数"])
    writer.writerow(["张三",20,85])
    writer.writerow(["李四", 21, 86])
    writer.writerow(["王五",22,88])
print("已写入students.csv")

with open("students.csv","r",encoding="utf-8-sig",newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['姓名']},{row['年龄']}岁,{row['分数']}分")


def analyze_text(filepath):
    with open(filepath,"r",encoding="utf-8") as f:
        lines=f.readlines()
    count=0
    words={}
    for line in lines:
        line=line.strip()
        parts = line.split(" ")
        parts = [p.strip('.,!?;:""()[]') for p in parts if p.strip('.,!?;:""()[]')]
        count+=len(parts)
        for part in parts:
            if part not in words:
                words[part]=1
            else:
                words[part]+=1
    count_different=len(words)
    words_sorted=sorted(words.items(),key=lambda x:x[1],reverse=True)
    return f"总单词数:{count},不同单词数:{count_different},出现次数最多的3个单词（及其次数）:{words_sorted[:3]}"

print(analyze_text("words_test.txt"))