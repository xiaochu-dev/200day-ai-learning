"""
Day 19 — Python + SQLite 基础练习（参考答案）
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "day19_test.db")


def cleanup():
    try:
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
    except PermissionError:
        pass  # Windows 文件锁定延迟，忽略


def task1_create_and_insert():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # 创建用户表
        cur.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT UNIQUE,
                city TEXT
            )
        """)

        # 插入初始数据
        users = [
            (1, '张三', 25, 'zhangsan@qq.com', '北京'),
            (2, '李四', 30, 'lisi@qq.com', '上海'),
            (3, '王五', 28, 'wangwu@qq.com', '北京'),
            (4, '赵六', 22, 'zhaoliu@qq.com', '广州'),
        ]
        cur.executemany(
            "INSERT INTO users (id, name, age, email, city) VALUES (?, ?, ?, ?, ?)",
            users
        )
        # with 结尾自动 commit


def task2_query_by_city(city: str):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        # 参数化查询：用 ? 占位符，防 SQL 注入
        cur.execute(
            "SELECT name, age, email, city FROM users WHERE city = ?",
            (city,)
        )
        return cur.fetchall()


def task3_crud():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # 1. CREATE：插入孙七
        cur.execute(
            "INSERT INTO users (name, age, email, city) VALUES (?, ?, ?, ?)",
            ("孙七", 26, "sunqi@qq.com", "深圳")
        )
        new_id = cur.lastrowid

        # 2. READ：查出孙七
        cur.execute("SELECT name, age, email, city FROM users WHERE id = ?", (new_id,))
        new_user = cur.fetchone()

        # 3. UPDATE：改年龄
        cur.execute("UPDATE users SET age = ? WHERE id = ?", (27, new_id))

        # 再查一次看更新结果
        cur.execute("SELECT name, age, email, city FROM users WHERE id = ?", (new_id,))
        updated_user = cur.fetchone()

        # 4. DELETE：删除赵六
        cur.execute("DELETE FROM users WHERE id = 4")

        return (new_user, updated_user)


def task4_to_dict_list():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, age, email, city FROM users")
        rows = cur.fetchall()

        # 从 cur.description 获取列名
        columns = [desc[0] for desc in cur.description]

        # 将每一行 tuple 转成 dict
        result = [dict(zip(columns, row)) for row in rows]
        return result


if __name__ == "__main__":
    cleanup()

    print("=" * 50)
    print("Day 19 — Python + SQLite 基础（参考答案）")
    print("=" * 50)

    # 任务1
    print("\n[任务1] 创建数据库和表...")
    task1_create_and_insert()
    assert os.path.exists(DB_PATH), "❌ 数据库文件未创建！"
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]
    conn.close()
    assert count == 4, f"❌ 期望 4 条数据，实际 {count} 条"
    print(f"  ✅ 通过！(已插入 {count} 条数据)")

    # 任务2
    print("\n[任务2] 按城市查询（北京）...")
    result = task2_query_by_city("北京")
    assert len(result) == 2, f"❌ 期望 2 个北京用户，实际 {len(result)} 个"
    print(f"  查询到 {len(result)} 个北京用户：")
    for row in result:
        print(f"    {row}")
    print("  ✅ 通过！")

    # 任务3
    print("\n[任务3] CRUD 操作...")
    new_user, updated_user = task3_crud()
    assert new_user is not None, "❌ 插入失败"
    assert new_user[0] == "孙七", f"❌ 期望孙七，实际 {new_user[0]}"
    print(f"  插入: {new_user}")
    assert updated_user[1] == 27, f"❌ 期望年龄 27，实际 {updated_user[1]}"
    print(f"  更新后: {updated_user}")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = 4")
    deleted = cur.fetchone()
    conn.close()
    assert deleted is None, "❌ 赵六未被删除！"
    print("  ✅ 通过！")

    # 任务4
    print("\n[任务4] 结果转字典列表...")
    users = task4_to_dict_list()
    assert isinstance(users, list), "❌ 返回值不是 list"
    assert isinstance(users[0], dict), "❌ 列表元素不是 dict"
    assert "name" in users[0], "❌ 字典缺少 'name' 键"
    print(f"  共 {len(users)} 个用户：")
    for u in users:
        print(f"    {u}")
    print("  ✅ 通过！")

    cleanup()
    print("\n🎉 全部通过！")
