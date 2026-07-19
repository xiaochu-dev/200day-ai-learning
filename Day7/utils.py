"""
Day7 — utils.py
@log_call 装饰器 + 日志工具

⚠️ 本文件是需要你动手填写的练习模板，每个 `# TODO:` 需要补全。
"""

from functools import wraps
from datetime import datetime


# ============================================================
# TODO 1: @log_call 装饰器
# ============================================================
def log_call(func):
    """
    装饰器：每次被装饰的函数调用时，打印一行日志。

    日志格式：
    [2026-07-19 20:30:00] manage() 被调用

    提示：
    - 用 datetime.now().strftime("%Y-%m-%d %H:%M:%S") 获取时间戳
    - 用 func.__name__ 获取函数名
    - 别忘了 @wraps(func) 保留原函数元信息
    """
    # TODO: 实现装饰器
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}]{func.__name__}()被调用")
        result = func(*args, **kwargs)
        return result
    return wrapper


# ============================================================
# TODO 2: 日志文件写入（选做）
# ============================================================
LOG_FILE = "server.log"


def write_log(message):
    """
    将日志信息追加写入 LOG_FILE

    要求：
    - 用 with open(...) 以追加模式打开
    - 每行一条日志
    - 如果文件不存在则自动创建
    """
    # TODO: 实现日志写入
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")


# ============================================================
# 参考答案
# ============================================================
"""
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {func.__name__}() 被调用")
        result = func(*args, **kwargs)
        return result
    return wrapper


def write_log(message):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
"""
