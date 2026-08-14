"""
Day 17 — 多表 JOIN + 子查询练习

运行方式：直接运行本文件即可
python Day17_sql_join.py

场景：电商系统 —— 用户表 + 订单表
"""

import sqlite3


def init_db():
    """创建用户表和订单表"""
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
        (1, '张三', '杭州', 2),
        (2, '李四', '上海', 1),
        (3, '王五', '杭州', 0),
        (4, '赵六', '北京', 3),
        (5, '孙七', '上海', 0),
    ]
    cur.executemany(
        "INSERT INTO users VALUES (?, ?, ?, ?)", users
    )

    orders = [
        (1, 1, 'iPhone 15', 6999.0, '2026-07-01'),
        (2, 1, 'AirPods', 1299.0, '2026-07-15'),
        (3, 2, 'MacBook Pro', 14999.0, '2026-07-10'),
        (4, 4, '机械键盘', 399.0, '2026-07-20'),
        (5, 4, '显示器', 2499.0, '2026-07-22'),
        (6, 4, '鼠标', 149.0, '2026-08-01'),
        # 注意：王五(3)和孙七(5)没有订单
    ]
    cur.executemany(
        "INSERT INTO orders VALUES (?, ?, ?, ?, ?)", orders
    )
    conn.commit()
    return conn


# ============================================================
# TODO 1：INNER JOIN —— 查每个用户的订单
# ============================================================
def task1_inner_join(conn):
    """
    查询每个用户的订单，返回 (user_name, product, amount)，
    按 user_name 排序，同名再按 amount 降序。

    提示：INNER JOIN ... ON users.id = orders.user_id

    预期：只有有订单的用户出现（张三2条、李四1条、赵六3条）
    共6条，王五和孙七不出现。
    """
    cur = conn.cursor()
    # TODO: 写 INNER JOIN 查询
    cur.execute("""
        -- 在这里写你的 SQL
    """)
    return cur.fetchall()


# ============================================================
# TODO 2：LEFT JOIN —— 包含没有订单的用户
# ============================================================
def task2_left_join(conn):
    """
    查询所有用户及其订单总金额（没订单的显示 0 或 NULL）。
    返回 (user_name, vip_level, total_amount)，按 total_amount 降序。

    提示：LEFT JOIN + GROUP BY + COALESCE(SUM(amount), 0) 处理 NULL

    预期：
    [('赵六', 3, 3047.0), ('张三', 2, 8298.0), ('李四', 1, 14999.0),
     ('王五', 0, 0.0), ('孙七', 0, 0.0)]
    """
    cur = conn.cursor()
    # TODO: 写 LEFT JOIN 查询
    cur.execute("""
        -- 在这里写你的 SQL
    """)
    return cur.fetchall()


# ============================================================
# TODO 3：GROUP BY + HAVING
# ============================================================
def task3_groupby_having(conn):
    """
    查询"消费总额 >= 5000"的用户，
    返回 (user_name, order_count, total_amount)。

    提示：先 INNER JOIN，再 GROUP BY user_id，再用 HAVING 筛选

    预期：
    [('张三', 2, 8298.0), ('李四', 1, 14999.0)]
    """
    cur = conn.cursor()
    # TODO: 写 GROUP BY + HAVING 查询
    cur.execute("""
        -- 在这里写你的 SQL
    """)
    return cur.fetchall()


# ============================================================
# TODO 4：子查询
# ============================================================
def task4_subquery(conn):
    """
    查询"消费高于人均消费额"的用户，
    返回 (user_name, total_amount)。

    思路：
    1. 子查询算出所有订单的人均消费 = SUM(amount) / COUNT(DISTINCT user_id)
    2. 外层查询按用户汇总，筛选 total > 人均

    所有用户的总消费（只有3人有订单）：
    - 张三: 8298, 李四: 14999, 赵六: 3047, 王五: 0, 孙七: 0
    有订单的人均 = (8298+14999+3047) / 3 ≈ 8781.33

    预期（总消费 > 8781.33）：
    [('李四', 14999.0)]
    """
    cur = conn.cursor()
    # TODO: 写子查询
    cur.execute("""
        -- 在这里写你的 SQL
    """)
    return cur.fetchall()


# ============================================================
# 测试运行
# ============================================================
if __name__ == "__main__":
    conn = init_db()
    print("=" * 50)
    print("Day 17 — 多表 JOIN + 子查询练习")
    print("=" * 50)

    print("\n[任务1] INNER JOIN —— 用户订单：")
    result = task1_inner_join(conn)
    for row in result:
        print(f"  {row[0]} → {row[1]} (¥{row[2]})")
    expected = [
        ('张三', 'iPhone 15', 6999.0), ('张三', 'AirPods', 1299.0),
        ('李四', 'MacBook Pro', 14999.0),
        ('赵六', '显示器', 2499.0), ('赵六', '机械键盘', 399.0), ('赵六', '鼠标', 149.0),
    ]
    assert result == expected, f"❌ 不通过！\n期望: {expected}\n实际: {result}"
    print(f"  ✅ 通过！共 {len(result)} 条")

    print("\n[任务2] LEFT JOIN —— 全部用户+消费总额：")
    result = task2_left_join(conn)
    for row in result:
        print(f"  {row[0]} (VIP{row[1]}): ¥{row[2]}")
    expected = [
        ('李四', 1, 14999.0), ('张三', 2, 8298.0), ('赵六', 3, 3047.0),
        ('王五', 0, 0.0), ('孙七', 0, 0.0),
    ]
    assert result == expected, f"❌ 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    print("\n[任务3] GROUP BY + HAVING（>=5000）：")
    result = task3_groupby_having(conn)
    for row in result:
        print(f"  {row[0]}: {row[1]}单, ¥{row[2]}")
    expected = [('张三', 2, 8298.0), ('李四', 1, 14999.0)]
    assert result == expected, f"❌ 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    print("\n[任务4] 子查询 —— 高于人均消费：")
    result = task4_subquery(conn)
    for row in result:
        print(f"  {row[0]}: ¥{row[1]}")
    expected = [('李四', 14999.0)]
    assert result == expected, f"❌ 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    conn.close()
    print("\n🎉 全部通过！Day 17 JOIN+子查询完成！")
