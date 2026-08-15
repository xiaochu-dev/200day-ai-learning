"""
Day 20 — Python 数据库操作进阶练习

运行方式：直接运行本文件即可
python Day20_python_sqlite_adv.py
"""

import sqlite3
import os
import csv
import time

DB_PATH = os.path.join(os.path.dirname(__file__), "day20_test.db")


def cleanup():
    try:
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
    except PermissionError:
        pass  # Windows 文件锁定延迟，忽略


# ============================================================
# 初始化数据库（创建 accounts 表和 users 表）
# ============================================================
def init_db():
    """创建初始数据库，供后续任务使用"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 账户表（用于事务转账练习）
    cur.execute("""
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    """)
    cur.executemany(
        "INSERT INTO accounts VALUES (?, ?, ?)",
        [(1, '张三', 10000.0), (2, '李四', 5000.0), (3, '王五', 3000.0)],
    )

    # 用户表（用于 DAO 练习）
    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE,
            city TEXT
        )
    """)
    cur.executemany(
        "INSERT INTO users (id, name, age, email, city) VALUES (?, ?, ?, ?, ?)",
        [
            (1, '张三', 25, 'zhangsan@qq.com', '北京'),
            (2, '李四', 30, 'lisi@qq.com', '上海'),
            (3, '王五', 28, 'wangwu@qq.com', '北京'),
            (4, '赵六', 22, 'zhaoliu@qq.com', '广州'),
        ],
    )

    conn.commit()
    conn.close()


# ============================================================
# TODO 1：事务操作——转账
# ============================================================
def task1_transfer(from_id: int, to_id: int, amount: float):
    """
    要求：
    1. 从一个账户扣钱，给另一个账户加钱——两个 UPDATE 在同一个事务中
    2. 如果转出账户余额不足，抛出 ValueError，并回滚所有操作
    3. 如果目标账户不存在（UPDATE 影响 0 行），也要回滚
    4. 正常情况 commit，异常情况 rollback

    参数：
        from_id: 转出账户 id
        to_id: 转入账户 id
        amount: 转账金额

    返回：
        tuple (from_balance_after, to_balance_after) 转账后两个账户的余额

    提示：
        用 try/except/finally 结构
        先查询余额是否充足，再执行 UPDATE
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 2：批量插入 1000 条 + 性能对比
# ============================================================
def task2_batch_insert():
    """
    要求：
    1. 创建一张新表 batch_test (id INTEGER PRIMARY KEY, val TEXT)
    2. 方法A：逐条 insert + 每 100 条 commit（模拟逐条慢速）
    3. 方法B：executemany 一次性插入
    4. 两个方法各插入相同的 1000 条数据（val 为 "item_0" ~ "item_999"）
    5. 用 time.perf_counter() 计时

    返回：
        tuple (time_a_ms, time_b_ms) 两种方式的耗时（毫秒，保留3位小数）

    注意：每次测试前 DROP TABLE 再重新 CREATE，保证公平对比。
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 3：封装 UserDAO 类
# ============================================================
class UserDAO:
    """
    要求：实现以下 6 个方法，每个方法内部用 with sqlite3.connect() 管理连接

    - __init__(self, db_path): 保存数据库路径
    - create(self, name, age, email, city) -> int: 插入新用户，返回新 id
    - read(self, user_id) -> dict or None: 按 id 查用户，返回字典(含5个字段)或 None
    - update(self, user_id, **kwargs) -> bool: 按 id 更新（kwargs 如 age=30, city='上海'），返回是否成功
    - delete(self, user_id) -> bool: 按 id 删除，返回是否成功
    - find_by_city(self, city) -> list[dict]: 按城市查找，返回字典列表
    """

    def __init__(self, db_path: str):
        # TODO: 保存路径
        pass

    def create(self, name: str, age: int, email: str, city: str) -> int:
        # TODO: 插入新用户，返回 lastrowid
        pass

    def read(self, user_id: int) -> dict | None:
        # TODO: 查询并返回字典，查不到返回 None
        pass

    def update(self, user_id: int, **kwargs) -> bool:
        # TODO: 动态构建 SET 子句，更新用户
        pass

    def delete(self, user_id: int) -> bool:
        # TODO: 删除用户，返回是否成功
        pass

    def find_by_city(self, city: str) -> list[dict]:
        # TODO: 按城市查询，返回字典列表
        pass


# ============================================================
# TODO 4：查询结果导出 CSV
# ============================================================
def task4_export_csv(output_path: str):
    """
    要求：
    1. 查询 users 表所有数据（id, name, age, email, city）
    2. 写入 CSV 文件到 output_path
    3. CSV 要包含表头行
    4. 编码用 utf-8-sig（Excel 可直接打开不乱码）

    参数：
        output_path: CSV 输出路径

    返回：无（生成 CSV 文件即可）
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# 测试运行（不需要修改）
# ============================================================
if __name__ == "__main__":
    cleanup()
    init_db()

    print("=" * 50)
    print("Day 20 — SQLite 进阶练习")
    print("=" * 50)

    # 任务1：转账成功
    print("\n[任务1] 转账：张三 → 李四 2000 元")
    b1, b2 = task1_transfer(1, 2, 2000)
    print(f"  张三余额: {b1}, 李四余额: {b2}")
    assert b1 == 8000.0, f"❌ 张三余额应为 8000，实际 {b1}"
    assert b2 == 7000.0, f"❌ 李四余额应为 7000，实际 {b2}"
    print("  ✅ 转账成功！")

    # 任务1：余额不足回滚
    print("\n[任务1] 转账失败回滚：张三 → 王五 90000 元")
    try:
        task1_transfer(1, 3, 90000)
        print("  ❌ 应该抛出异常但没有！")
        assert False
    except ValueError as e:
        print(f"  正确抛出异常: {e}")
    # 验证余额没变
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE id = 1")
    b1_after = cur.fetchone()[0]
    conn.close()
    assert b1_after == 8000.0, f"❌ 回滚失败！余额从 8000 变成了 {b1_after}"
    print("  ✅ 回滚成功，余额未变！")

    # 任务2：批量插入性能
    print("\n[任务2] 批量插入性能对比...")
    t_a, t_b = task2_batch_insert()
    print(f"  逐条插入: {t_a}ms")
    print(f"  executemany: {t_b}ms")
    if t_b > 0:
        print(f"  加速比: {t_a/t_b:.1f}x")
    assert t_a >= 0 and t_b >= 0, "❌ 计时异常"
    print("  ✅ 通过！")

    # 任务3：UserDAO
    print("\n[任务3] UserDAO 测试...")
    dao = UserDAO(DB_PATH)

    # create
    new_id = dao.create("孙七", 26, "sunqi@qq.com", "深圳")
    assert new_id == 5, f"❌ 期望 id=5，实际 {new_id}"
    print(f"  创建 孙七 id={new_id}")

    # read
    user = dao.read(new_id)
    assert user["name"] == "孙七", f"❌ 期望孙七，实际 {user['name']}"
    assert user["city"] == "深圳"
    print(f"  读取: {user}")

    # update
    ok = dao.update(new_id, age=27, city="杭州")
    assert ok, "❌ 更新失败"
    user = dao.read(new_id)
    assert user["age"] == 27 and user["city"] == "杭州"
    print(f"  更新后: {user}")

    # find_by_city
    beijing_users = dao.find_by_city("北京")
    assert len(beijing_users) == 2
    print(f"  北京用户 {len(beijing_users)} 人: {[u['name'] for u in beijing_users]}")

    # delete
    ok = dao.delete(new_id)
    assert ok, "❌ 删除失败"
    assert dao.read(new_id) is None, "❌ 删除后还能查到！"
    print(f"  删除 孙七 成功")
    print("  ✅ 通过！")

    # 任务4：CSV导出
    print("\n[任务4] CSV 导出...")
    csv_path = os.path.join(os.path.dirname(__file__), "day20_users.csv")
    task4_export_csv(csv_path)
    assert os.path.exists(csv_path), "❌ CSV 文件未生成！"
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
    assert len(lines) >= 5, f"❌ CSV 行数不足，期望至少5行（1表头+4数据），实际 {len(lines)}"
    print(f"  已导出 {len(lines)-1} 行数据到 {csv_path}")
    print(f"  表头: {lines[0].strip()}")
    print(f"  首行: {lines[1].strip()}")
    os.remove(csv_path)  # 清理导出文件
    print("  ✅ 通过！")

    cleanup()
    print("\n🎉 全部通过！Day 20 SQLite 进阶完成！")
