"""
Day 16 — SQL 增删改 + 聚合函数练习（参考答案）

可直接运行：python Day16_sql_crud_答案.py
"""

import sqlite3


def init_db():
    conn = sqlite3.connect(":memory:")
    # 不使用 row_factory，保持结果为 tuple 便于 assert 比较
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            price REAL,
            stock INTEGER
        )
    """)

    data = [
        (1, 'iPhone 15', '电子产品', 6999.0, 50),
        (2, 'MacBook Pro', '电子产品', 14999.0, 30),
        (3, 'Python编程', '图书', 79.0, 200),
        (4, '算法导论', '图书', 128.0, 80),
        (5, '机械键盘', '电子产品', 399.0, 150),
        (6, '数据结构', '图书', 59.0, 120),
        (7, '显示器', '电子产品', 2499.0, 25),
        (8, '深度学习', '图书', 99.0, 60),
    ]
    cur.executemany(
        "INSERT INTO products (id, name, category, price, stock) VALUES (?, ?, ?, ?, ?)",
        data,
    )
    conn.commit()
    return conn


def task1_insert(conn):
    """插入数据"""
    cur = conn.cursor()
    # 单条插入
    cur.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        ('无线鼠标', '电子产品', 149.0, 300),
    )
    # 批量插入
    cur.executemany(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        [
            ('Java核心技术', '图书', 109.0, 45),
            ('人体工学椅', '家具', 2999.0, 10),
        ],
    )
    conn.commit()
    cur.execute("SELECT id, name, category, price FROM products ORDER BY id")
    return cur.fetchall()


def task2_update(conn):
    """更新数据"""
    cur = conn.cursor()
    # 更新"Python编程"价格
    cur.execute("UPDATE products SET price = 89.0 WHERE name = 'Python编程'")
    # 电子产品库存减5
    cur.execute("UPDATE products SET stock = stock - 5 WHERE category = '电子产品'")
    conn.commit()
    # 查询"Python编程"和所有电子产品
    cur.execute("""
        SELECT name, price, stock
        FROM products
        WHERE name = 'Python编程' OR category = '电子产品'
        ORDER BY name
    """)
    return cur.fetchall()


def task3_delete(conn):
    """删除库存<=0的产品"""
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE stock <= 0")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM products")
    return cur.fetchone()[0]


def task4_aggregation(conn):
    """按品类聚合统计"""
    cur = conn.cursor()
    cur.execute("""
        SELECT
            category,
            COUNT(*) as cnt,
            AVG(price) as avg_price,
            MAX(price) as max_price,
            SUM(stock) as total_stock
        FROM products
        GROUP BY category
        ORDER BY avg_price DESC
    """)
    return cur.fetchall()


# ============================================================
if __name__ == "__main__":
    conn = init_db()
    print("=" * 50)
    print("Day 16 — SQL 增删改 + 聚合函数（参考答案）")
    print("=" * 50)

    print("\n[任务1] 插入数据后全部产品：")
    result = task1_insert(conn)
    for row in result:
        print(f"  #{row[0]} {row[1]} [{row[2]}] ¥{row[3]}")
    assert len(result) == 11
    print(f"  ✅ 通过！共 {len(result)} 条")

    print("\n[任务2] 更新后结果：")
    result = task2_update(conn)
    for row in result:
        print(f"  {row[0]}: ¥{row[1]}, 库存={row[2]}")
    expected = [
        ('MacBook Pro', 14999.0, 25), ('Python编程', 89.0, 200),
        ('iPhone 15', 6999.0, 45), ('无线鼠标', 149.0, 295),
        ('显示器', 2499.0, 20), ('机械键盘', 399.0, 145),
    ]
    assert result == expected
    print("  ✅ 通过！")

    print("\n[任务3] 删除库存<=0后剩余：")
    count = task3_delete(conn)
    print(f"  剩余产品数: {count}")
    assert count == 11
    print("  ✅ 通过！")

    print("\n[任务4] 按品类统计：")
    result = task4_aggregation(conn)
    for row in result:
        print(f"  {row[0]}: {row[1]}件, 均价¥{row[2]:.2f}, 最贵¥{row[3]}, 总库存{row[4]}")
    expected = [
        ('电子产品', 5, 5009.0, 14999.0, 530),
        ('家具', 1, 2999.0, 2999.0, 10),
        ('图书', 5, 96.80, 128.0, 505),
    ]
    assert result == expected
    print("  ✅ 通过！")

    conn.close()
    print("\n🎉 全部通过！")
