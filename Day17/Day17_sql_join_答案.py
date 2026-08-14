"""
Day 17 — 多表 JOIN + 子查询练习（参考答案）
"""

import sqlite3


def init_db():
    conn = sqlite3.connect(":memory:")
    # 不使用 row_factory，保持结果为 tuple 便于 assert 比较
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            city TEXT,
            vip_level INTEGER DEFAULT 0
        )
    """)
    cur.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            product TEXT,
            amount REAL,
            order_date TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    users = [
        (1, '张三', '杭州', 2), (2, '李四', '上海', 1),
        (3, '王五', '杭州', 0), (4, '赵六', '北京', 3), (5, '孙七', '上海', 0),
    ]
    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", users)

    orders = [
        (1, 1, 'iPhone 15', 6999.0, '2026-07-01'),
        (2, 1, 'AirPods', 1299.0, '2026-07-15'),
        (3, 2, 'MacBook Pro', 14999.0, '2026-07-10'),
        (4, 4, '机械键盘', 399.0, '2026-07-20'),
        (5, 4, '显示器', 2499.0, '2026-07-22'),
        (6, 4, '鼠标', 149.0, '2026-08-01'),
    ]
    cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", orders)
    conn.commit()
    return conn


def task1_inner_join(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT u.name, o.product, o.amount
        FROM users u
        INNER JOIN orders o ON u.id = o.user_id
        ORDER BY u.name, o.amount DESC
    """)
    return cur.fetchall()


def task2_left_join(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT u.name, u.vip_level,
               COALESCE(SUM(o.amount), 0) as total_amount
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        GROUP BY u.id
        ORDER BY total_amount DESC
    """)
    return cur.fetchall()


def task3_groupby_having(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT u.name, COUNT(o.id) as order_count,
               SUM(o.amount) as total_amount
        FROM users u
        INNER JOIN orders o ON u.id = o.user_id
        GROUP BY u.id
        HAVING total_amount >= 5000
    """)
    return cur.fetchall()


def task4_subquery(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT u.name, SUM(o.amount) as total_amount
        FROM users u
        INNER JOIN orders o ON u.id = o.user_id
        GROUP BY u.id
        HAVING total_amount > (
            SELECT SUM(amount) / COUNT(DISTINCT user_id)
            FROM orders
        )
    """)
    return cur.fetchall()


if __name__ == "__main__":
    conn = init_db()
    print("=" * 50)
    print("Day 17 — 多表 JOIN + 子查询（参考答案）")
    print("=" * 50)

    print("\n[任务1] INNER JOIN：")
    result = task1_inner_join(conn)
    for row in result:
        print(f"  {row[0]} → {row[1]} (¥{row[2]})")
    expected = [
        ('张三', 'iPhone 15', 6999.0), ('张三', 'AirPods', 1299.0),
        ('李四', 'MacBook Pro', 14999.0),
        ('赵六', '显示器', 2499.0), ('赵六', '机械键盘', 399.0), ('赵六', '鼠标', 149.0),
    ]
    assert result == expected
    print(f"  ✅ 通过！共 {len(result)} 条")

    print("\n[任务2] LEFT JOIN：")
    result = task2_left_join(conn)
    for row in result:
        print(f"  {row[0]} (VIP{row[1]}): ¥{row[2]}")
    expected = [
        ('李四', 1, 14999.0), ('张三', 2, 8298.0), ('赵六', 3, 3047.0),
        ('王五', 0, 0.0), ('孙七', 0, 0.0),
    ]
    assert result == expected
    print("  ✅ 通过！")

    print("\n[任务3] GROUP BY + HAVING：")
    result = task3_groupby_having(conn)
    for row in result:
        print(f"  {row[0]}: {row[1]}单, ¥{row[2]}")
    expected = [('张三', 2, 8298.0), ('李四', 1, 14999.0)]
    assert result == expected
    print("  ✅ 通过！")

    print("\n[任务4] 子查询：")
    result = task4_subquery(conn)
    for row in result:
        print(f"  {row[0]}: ¥{row[1]}")
    expected = [('李四', 14999.0)]
    assert result == expected
    print("  ✅ 通过！")

    conn.close()
    print("\n🎉 全部通过！")
