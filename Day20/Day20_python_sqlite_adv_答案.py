"""
Day 20 — Python 数据库操作进阶（参考答案）
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


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 账户表
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

    # 用户表
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
# 任务1：事务——转账
# ============================================================
def task1_transfer(from_id: int, to_id: int, amount: float):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        # 1. 检查转出账户余额
        cur.execute("SELECT balance FROM accounts WHERE id = ?", (from_id,))
        row = cur.fetchone()
        if row is None:
            raise ValueError(f"账户 {from_id} 不存在")
        if row[0] < amount:
            raise ValueError(f"账户 {from_id} 余额不足（当前 {row[0]}，需要 {amount}）")

        # 2. 检查转入账户是否存在
        cur.execute("SELECT id FROM accounts WHERE id = ?", (to_id,))
        if cur.fetchone() is None:
            raise ValueError(f"账户 {to_id} 不存在")

        # 3. 执行转账（两个 UPDATE）
        cur.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, from_id)
        )
        cur.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, to_id)
        )

        conn.commit()

        # 4. 查询转账后余额
        cur.execute("SELECT balance FROM accounts WHERE id = ?", (from_id,))
        from_balance = cur.fetchone()[0]
        cur.execute("SELECT balance FROM accounts WHERE id = ?", (to_id,))
        to_balance = cur.fetchone()[0]

        return (from_balance, to_balance)

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


# ============================================================
# 任务2：批量插入性能对比
# ============================================================
def task2_batch_insert():
    data = [("item_" + str(i),) for i in range(1000)]

    # 方法A：逐条插入
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS batch_test_a")
    cur.execute("CREATE TABLE batch_test_a (id INTEGER PRIMARY KEY AUTOINCREMENT, val TEXT)")
    conn.commit()

    start = time.perf_counter()
    for i, item in enumerate(data):
        cur.execute("INSERT INTO batch_test_a (val) VALUES (?)", item)
        if (i + 1) % 100 == 0:
            conn.commit()
    conn.commit()
    time_a = (time.perf_counter() - start) * 1000
    conn.close()

    # 方法B：executemany
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS batch_test_b")
    cur.execute("CREATE TABLE batch_test_b (id INTEGER PRIMARY KEY AUTOINCREMENT, val TEXT)")

    start = time.perf_counter()
    cur.executemany("INSERT INTO batch_test_b (val) VALUES (?)", data)
    conn.commit()
    time_b = (time.perf_counter() - start) * 1000
    conn.close()

    return (round(time_a, 3), round(time_b, 3))


# ============================================================
# 任务3：UserDAO 类
# ============================================================
class UserDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def create(self, name: str, age: int, email: str, city: str) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (name, age, email, city) VALUES (?, ?, ?, ?)",
                (name, age, email, city)
            )
            return cur.lastrowid

    def read(self, user_id: int) -> dict | None:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, name, age, email, city FROM users WHERE id = ?", (user_id,))
            row = cur.fetchone()
            if row is None:
                return None
            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))

    def update(self, user_id: int, **kwargs) -> bool:
        if not kwargs:
            return False

        # 动态构建 SET 子句：SET age=?, city=?
        set_parts = [f"{col} = ?" for col in kwargs.keys()]
        set_sql = ", ".join(set_parts)
        values = list(kwargs.values()) + [user_id]

        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                f"UPDATE users SET {set_sql} WHERE id = ?",
                values
            )
            return cur.rowcount > 0

    def delete(self, user_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
            return cur.rowcount > 0

    def find_by_city(self, city: str) -> list[dict]:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, name, age, email, city FROM users WHERE city = ?", (city,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]


# ============================================================
# 任务4：导出 CSV
# ============================================================
def task4_export_csv(output_path: str):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, age, email, city FROM users")
        rows = cur.fetchall()

    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "age", "email", "city"])
        writer.writerows(rows)


# ============================================================
# 测试运行
# ============================================================
if __name__ == "__main__":
    cleanup()
    init_db()

    print("=" * 50)
    print("Day 20 — SQLite 进阶（参考答案）")
    print("=" * 50)

    # 任务1
    print("\n[任务1] 转账：张三 → 李四 2000 元")
    b1, b2 = task1_transfer(1, 2, 2000)
    print(f"  张三余额: {b1}, 李四余额: {b2}")
    assert b1 == 8000.0
    assert b2 == 7000.0
    print("  ✅ 转账成功！")

    print("\n[任务1] 转账失败回滚：张三 → 王五 90000 元")
    try:
        task1_transfer(1, 3, 90000)
        assert False, "应抛异常"
    except ValueError as e:
        print(f"  正确抛出异常: {e}")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE id = 1")
    b1_after = cur.fetchone()[0]
    conn.close()
    assert b1_after == 8000.0
    print("  ✅ 回滚成功！")

    # 任务2
    print("\n[任务2] 批量插入性能...")
    t_a, t_b = task2_batch_insert()
    print(f"  逐条插入: {t_a}ms")
    print(f"  executemany: {t_b}ms")
    if t_b > 0:
        print(f"  加速比: {t_a/t_b:.1f}x")
    print("  ✅ 通过！")

    # 任务3
    print("\n[任务3] UserDAO 测试...")
    dao = UserDAO(DB_PATH)

    new_id = dao.create("孙七", 26, "sunqi@qq.com", "深圳")
    print(f"  创建 孙七 id={new_id}")

    user = dao.read(new_id)
    print(f"  读取: {user}")

    dao.update(new_id, age=27, city="杭州")
    user = dao.read(new_id)
    print(f"  更新后: {user}")

    beijing_users = dao.find_by_city("北京")
    print(f"  北京用户: {[u['name'] for u in beijing_users]}")

    dao.delete(new_id)
    assert dao.read(new_id) is None
    print(f"  删除成功")
    print("  ✅ 通过！")

    # 任务4
    print("\n[任务4] CSV 导出...")
    csv_path = os.path.join(os.path.dirname(__file__), "day20_users.csv")
    task4_export_csv(csv_path)
    assert os.path.exists(csv_path)
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
    print(f"  已导出 {len(lines)-1} 行数据")
    print(f"  表头: {lines[0].strip()}")
    print(f"  首行: {lines[1].strip()}")
    os.remove(csv_path)
    print("  ✅ 通过！")

    cleanup()
    print("\n🎉 全部通过！")
