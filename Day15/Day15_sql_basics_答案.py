"""
Day 15 — SQL 基础查询练习（参考答案）

可直接运行：python Day15_sql_basics_答案.py
"""

import sqlite3


def init_db():
    """创建内存数据库并插入测试数据"""
    conn = sqlite3.connect(":memory:")
    # 不使用 row_factory，保持结果为 tuple 便于 assert 比较
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT,
            score REAL,
            city TEXT
        )
    """)

    data = [
        (1, '张三', 20, 'A', 92.5, '杭州'),
        (2, '李四', 22, 'B', 78.0, '上海'),
        (3, '王五', 19, 'A', 88.5, '杭州'),
        (4, '赵六', 21, 'C', 65.0, '北京'),
        (5, '孙七', 20, 'B', 81.0, '上海'),
        (6, '周八', 23, 'A', 95.0, '杭州'),
        (7, '吴九', 19, 'C', 55.5, '北京'),
        (8, '郑十', 22, 'B', 76.5, '杭州'),
        (9, '钱十一', 20, 'A', 90.0, '上海'),
        (10, '陈十二', 21, 'C', 62.0, '北京'),
    ]
    cur.executemany(
        "INSERT INTO students (id, name, age, grade, score, city) VALUES (?, ?, ?, ?, ?, ?)",
        data,
    )
    conn.commit()
    return conn


def task1_select_high_scores(conn):
    """查询 score >= 80 的学生，按分数降序"""
    cur = conn.cursor()
    cur.execute("""
        SELECT name, score
        FROM students
        WHERE score >= 80
        ORDER BY score DESC
    """)
    return cur.fetchall()


def task2_like_search(conn):
    """模糊查询名字含"三"的学生"""
    cur = conn.cursor()
    cur.execute("""
        SELECT id, name, city
        FROM students
        WHERE name LIKE '%三%'
    """)
    return cur.fetchall()


def task3_in_and_between(conn):
    """IN + BETWEEN 组合查询"""
    cur = conn.cursor()
    cur.execute("""
        SELECT name, age, city, score
        FROM students
        WHERE city IN ('杭州', '上海')
          AND age BETWEEN 20 AND 22
    """)
    return cur.fetchall()


def task4_pagination(conn, page, page_size):
    """分页查询"""
    cur = conn.cursor()
    offset = (page - 1) * page_size
    cur.execute("""
        SELECT id, name, score
        FROM students
        ORDER BY id
        LIMIT ? OFFSET ?
    """, (page_size, offset))
    return cur.fetchall()


# ============================================================
# 测试运行
# ============================================================
if __name__ == "__main__":
    conn = init_db()

    print("=" * 50)
    print("Day 15 — SQL 基础查询练习（参考答案）")
    print("=" * 50)

    print("\n[任务1] score >= 80，按分数降序：")
    result = task1_select_high_scores(conn)
    for row in result:
        print(f"  {row[0]}: {row[1]}")
    expected = [('周八', 95.0), ('张三', 92.5), ('钱十一', 90.0), ('王五', 88.5), ('孙七', 81.0)]
    assert result == expected
    print("  ✅ 通过！")

    print("\n[任务2] 名字含'三'的学生：")
    result = task2_like_search(conn)
    for row in result:
        print(f"  id={row[0]}, name={row[1]}, city={row[2]}")
    expected = [(1, '张三', '杭州')]
    assert result == expected
    print("  ✅ 通过！")

    print("\n[任务3] 杭州/上海 + 20~22岁：")
    result = task3_in_and_between(conn)
    for row in result:
        print(f"  {row[0]}, {row[1]}岁, {row[2]}, {row[3]}分")
    expected = [
        ('张三', 20, '杭州', 92.5), ('李四', 22, '上海', 78.0),
        ('孙七', 20, '上海', 81.0), ('郑十', 22, '杭州', 76.5), ('钱十一', 20, '上海', 90.0),
    ]
    assert result == expected
    print("  ✅ 通过！")

    print("\n[任务4] 分页测试（第2页，每页3条）：")
    result = task4_pagination(conn, 2, 3)
    for row in result:
        print(f"  id={row[0]}, name={row[1]}, score={row[2]}")
    expected = [(4, '赵六', 65.0), (5, '孙七', 81.0), (6, '周八', 95.0)]
    assert result == expected
    print("  ✅ 通过！")

    conn.close()
    print("\n🎉 全部通过！")
