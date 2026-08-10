"""
Day 15 — SQL 基础查询练习

运行方式：直接运行本文件即可（使用内存数据库，无需安装任何东西）
python Day15_sql_basics.py

你的任务：补全下面 4 个函数中的 TODO，让每个函数返回正确的查询结果。
"""

import sqlite3


# ============================================================
# 准备工作：创建测试数据（已写好，不用改）
# ============================================================
def init_db():
    """创建内存数据库并插入测试数据"""
    conn = sqlite3.connect(":memory:")
    # 不使用 row_factory，保持结果为 tuple 便于比较
    cur = conn.cursor()

    # 创建学生表
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

    # 插入测试数据
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


# ============================================================
# TODO 1：基础 SELECT + WHERE
# ============================================================
def task1_select_high_scores(conn):
    """
    查询 score >= 80 的所有学生，返回 (name, score) 列表，
    按 score 从高到低排序。

    预期结果：
    [('周八', 95.0), ('张三', 92.5), ('钱十一', 90.0), ('王五', 88.5), ('孙七', 81.0)]
    """
    cur = conn.cursor()
    # TODO: 写 SQL 查询
    # 提示：SELECT name, score FROM students WHERE ... ORDER BY ... DESC
    cur.execute("""
        -- 在这里写你的 SQL
    """)
    return cur.fetchall()


# ============================================================
# TODO 2：LIKE 模糊查询
# ============================================================
def task2_like_search(conn):
    """
    查询名字中包含"三"的学生，返回 (id, name, city)。
    提示：LIKE 中 % 匹配任意字符，所以 '%三%' 表示包含"三"。

    预期结果：
    [(1, '张三', '杭州')]
    """
    cur = conn.cursor()
    # TODO: 写 SQL 查询
    cur.execute("""
        -- 在这里写你的 SQL
    """)
    return cur.fetchall()


# ============================================================
# TODO 3：IN + BETWEEN
# ============================================================
def task3_in_and_between(conn):
    """
    查询城市在 ('杭州', '上海') 且 age BETWEEN 20 AND 22 的学生，
    返回 (name, age, city, score)。

    预期结果：
    [('张三', 20, '杭州', 92.5), ('李四', 22, '上海', 78.0),
     ('孙七', 20, '上海', 81.0), ('郑十', 22, '杭州', 76.5), ('钱十一', 20, '上海', 90.0)]
    """
    cur = conn.cursor()
    # TODO: 写 SQL 查询
    cur.execute("""
        -- 在这里写你的 SQL
    """)
    return cur.fetchall()


# ============================================================
# TODO 4：LIMIT 分页
# ============================================================
def task4_pagination(conn, page, page_size):
    """
    分页查询：返回第 page 页的学生，每页 page_size 条。
    按 id 升序排列。

    例如 page=1, page_size=3 → 返回 id 1,2,3
         page=2, page_size=3 → 返回 id 4,5,6

    返回 (id, name, score) 列表。

    提示：LIMIT 数量 OFFSET 偏移量
          OFFSET = (page - 1) * page_size
    """
    cur = conn.cursor()
    # TODO: 写 SQL 查询
    offset = None  # TODO: 计算 offset
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
    print("Day 15 — SQL 基础查询练习")
    print("=" * 50)

    # 测试 1
    print("\n[任务1] score >= 80，按分数降序：")
    result = task1_select_high_scores(conn)
    for row in result:
        print(f"  {row[0]}: {row[1]}")
    expected = [('周八', 95.0), ('张三', 92.5), ('钱十一', 90.0), ('王五', 88.5), ('孙七', 81.0)]
    assert result == expected, f"❌ 任务1 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    # 测试 2
    print("\n[任务2] 名字含'三'的学生：")
    result = task2_like_search(conn)
    for row in result:
        print(f"  id={row[0]}, name={row[1]}, city={row[2]}")
    expected = [(1, '张三', '杭州')]
    assert result == expected, f"❌ 任务2 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    # 测试 3
    print("\n[任务3] 杭州/上海 + 20~22岁：")
    result = task3_in_and_between(conn)
    for row in result:
        print(f"  {row[0]}, {row[1]}岁, {row[2]}, {row[3]}分")
    expected = [
        ('张三', 20, '杭州', 92.5), ('李四', 22, '上海', 78.0),
        ('孙七', 20, '上海', 81.0), ('郑十', 22, '杭州', 76.5), ('钱十一', 20, '上海', 90.0),
    ]
    assert result == expected, f"❌ 任务3 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    # 测试 4
    print("\n[任务4] 分页测试（第2页，每页3条）：")
    result = task4_pagination(conn, 2, 3)
    for row in result:
        print(f"  id={row[0]}, name={row[1]}, score={row[2]}")
    expected = [(4, '赵六', 65.0), (5, '孙七', 81.0), (6, '周八', 95.0)]
    assert result == expected, f"❌ 任务4 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    conn.close()
    print("\n🎉 全部通过！Day 15 SQL 基础完成！")
