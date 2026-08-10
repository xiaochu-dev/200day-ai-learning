"""
Day 16 — SQL 增删改 + 聚合函数练习

运行方式：直接运行本文件即可
python Day16_sql_crud.py

你的任务：补全下面 4 个函数中的 TODO。
"""

import sqlite3


def init_db():
    """创建内存数据库并插入初始数据"""
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


# ============================================================
# TODO 1：INSERT 插入数据
# ============================================================
def task1_insert(conn):
    """
    1. 插入一条新产品：('无线鼠标', '电子产品', 149.0, 300)
    2. 再批量插入两条：
       ('Java核心技术', '图书', 109.0, 45)
       ('人体工学椅', '家具', 2999.0, 10)
    3. 查询所有产品，返回 (id, name, category, price) 列表，按 id 升序

    预期：11条记录，新增3条
    """
    cur = conn.cursor()
    # TODO: 1. 插入单条
    # TODO: 2. 批量插入两条
    # TODO: 3. 查询全部
    cur.execute("SELECT id, name, category, price FROM products ORDER BY id")
    return cur.fetchall()


# ============================================================
# TODO 2：UPDATE 更新数据
# ============================================================
def task2_update(conn):
    """
    1. 把"Python编程"的价格涨到 89.0
    2. 把所有"电子产品"的库存减少 5（stock = stock - 5）
    3. 查询更新后的"Python编程"和所有电子产品，返回 (name, price, stock)

    预期（按name排序）：
    [('MacBook Pro', 14999.0, 25), ('Python编程', 89.0, 200),
     ('iPhone 15', 6999.0, 45), ('无线鼠标', 149.0, 295),
     ('显示器', 2499.0, 20), ('机械键盘', 399.0, 145)]
    """
    cur = conn.cursor()
    # TODO: 1. 更新"Python编程"价格
    # TODO: 2. 电子产品库存减5（注意：因为前面已插入了无线鼠标，电子产品有5种）
    # TODO: 3. 查询
    cur.execute("""
        -- 在这里写查询
    """)
    return cur.fetchall()


# ============================================================
# TODO 3：DELETE 删除数据
# ============================================================
def task3_delete(conn):
    """
    1. 删除库存为 0 或更少的产品
    2. 查询剩余产品数量

    提示：先检查哪些产品库存 <= 0，然后 DELETE
    注意：初始数据里没有库存<=0的，但 task2 中有些产品库存减了5。
    其实初始的8条中电子产品（4条）减5后都>0，所以如果没有库存<=0的，
    DELETE 不会删除任何行，COUNT 应该还是11。

    返回剩余产品总数。
    """
    cur = conn.cursor()
    # TODO: 1. 删除库存 <= 0 的产品
    # TODO: 2. 统计剩余数量
    cur.execute("-- 在这里写查询")
    result = cur.fetchone()
    return result[0] if result else 0


# ============================================================
# TODO 4：聚合函数 + GROUP BY
# ============================================================
def task4_aggregation(conn):
    """
    统计每个品类的：
    - 产品数量 (COUNT)
    - 平均价格 (AVG)
    - 最高价格 (MAX)
    - 总库存 (SUM)

    返回 (category, count, avg_price, max_price, total_stock)，
    按 avg_price 降序排列。

    预期（3个品类）：
    [('电子产品', 5, 5009.0, 14999.0, 530),
     ('家具', 1, 2999.0, 2999.0, 10),
     ('图书', 5, 96.80, 128.0, 505)]
    """
    cur = conn.cursor()
    # TODO: 写聚合查询
    cur.execute("""
        -- 在这里写你的 SQL
    """)
    return cur.fetchall()


# ============================================================
# 测试运行（不用改）
# ============================================================
if __name__ == "__main__":
    conn = init_db()
    print("=" * 50)
    print("Day 16 — SQL 增删改 + 聚合函数练习")
    print("=" * 50)

    # 测试 1
    print("\n[任务1] 插入数据后全部产品：")
    result = task1_insert(conn)
    for row in result:
        print(f"  #{row[0]} {row[1]} [{row[2]}] ¥{row[3]}")
    assert len(result) == 11, f"❌ 应有11条记录，实际{len(result)}"
    print(f"  ✅ 通过！共 {len(result)} 条")

    # 测试 2
    print("\n[任务2] 更新后结果：")
    result = task2_update(conn)
    for row in result:
        print(f"  {row[0]}: ¥{row[1]}, 库存={row[2]}")
    expected = [
        ('iPhone 15', 6999.0, 45), ('MacBook Pro', 14999.0, 25),
        ('Python编程', 89.0, 200), ('机械键盘', 399.0, 145),
        ('无线鼠标', 149.0, 295), ('显示器', 2499.0, 20),
    ]
    assert result == expected, f"❌ 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    # 测试 3
    print("\n[任务3] 删除库存<=0后剩余：")
    count = task3_delete(conn)
    print(f"  剩余产品数: {count}")
    assert count == 11, f"❌ 应剩余11条，实际{count}"
    print("  ✅ 通过！")

    # 测试 4
    print("\n[任务4] 按品类统计：")
    result = task4_aggregation(conn)
    for row in result:
        print(f"  {row[0]}: {row[1]}件, 均价¥{row[2]:.2f}, 最贵¥{row[3]}, 总库存{row[4]}")
    expected = [
        ('电子产品', 5, 5009.0, 14999.0, 530),
        ('家具', 1, 2999.0, 2999.0, 10),
        ('图书', 4, 88.75, 128.0, 505),
    ]
    assert result == expected, f"❌ 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    conn.close()
    print("\n🎉 全部通过！Day 16 SQL 增删改完成！")
