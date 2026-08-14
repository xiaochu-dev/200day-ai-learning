"""
Day 18 — 索引与约束练习（参考答案）
"""

import sqlite3
import time


def init_db():
    conn = sqlite3.connect(":memory:")
    # 不使用 row_factory，保持结果为 tuple 便于 assert 比较
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            location TEXT DEFAULT '杭州'
        )
    """)
    cur.executemany(
        "INSERT INTO departments (id, name, location) VALUES (?, ?, ?)",
        [(1, '技术部', '杭州'), (2, '市场部', '上海'), (3, '人事部', '北京')],
    )

    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            salary REAL CHECK(salary > 0),
            dept_id INTEGER,
            FOREIGN KEY (dept_id) REFERENCES departments(id)
        )
    """)
    employees = [
        (1, '张三', 'zhangsan@qq.com', 15000.0, 1),
        (2, '李四', 'lisi@qq.com', 18000.0, 1),
        (3, '王五', 'wangwu@qq.com', 12000.0, 2),
        (4, '赵六', 'zhaoliu@qq.com', 20000.0, 2),
    ]
    cur.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employees)
    conn.commit()

    cur.execute("""
        CREATE TABLE big_table (
            id INTEGER PRIMARY KEY,
            name TEXT,
            value INTEGER
        )
    """)
    for i in range(10000):
        cur.execute(
            "INSERT INTO big_table (name, value) VALUES (?, ?)",
            (f"item_{i}", i % 1000),
        )
    conn.commit()
    return conn


def task1_constraints(conn):
    cur = conn.cursor()
    results = []

    # 测试1：UNIQUE 约束
    try:
        cur.execute(
            "INSERT INTO employees (id, name, email, salary, dept_id) VALUES (?, ?, ?, ?, ?)",
            (5, '测试1', 'zhangsan@qq.com', 10000.0, 1),
        )
        results.append("成功")
    except Exception as e:
        results.append(str(e)[:30])

    # 测试2：CHECK 约束
    try:
        cur.execute(
            "INSERT INTO employees (id, name, email, salary, dept_id) VALUES (?, ?, ?, ?, ?)",
            (6, '测试2', 'test2@qq.com', -500.0, 1),
        )
        results.append("成功")
    except Exception as e:
        results.append(str(e)[:30])

    # 测试3：外键约束
    try:
        cur.execute(
            "INSERT INTO employees (id, name, email, salary, dept_id) VALUES (?, ?, ?, ?, ?)",
            (7, '测试3', 'test3@qq.com', 10000.0, 99),
        )
        results.append("成功")
    except Exception as e:
        results.append(str(e)[:30])

    return tuple(results)


def task2_explain(conn):
    cur = conn.cursor()
    cur.execute("CREATE INDEX IF NOT EXISTS idx_big_name ON big_table(name)")
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM big_table WHERE name = 'item_5000'")
    return [str(row) for row in cur.fetchall()]


def task3_index_performance(conn):
    cur = conn.cursor()

    # 无索引查询
    start = time.perf_counter()
    cur.execute("SELECT COUNT(*) FROM big_table WHERE value = 500")
    cur.fetchall()
    time_no_index = (time.perf_counter() - start) * 1000

    # 创建索引
    cur.execute("CREATE INDEX IF NOT EXISTS idx_big_value ON big_table(value)")

    # 有索引查询
    start = time.perf_counter()
    cur.execute("SELECT COUNT(*) FROM big_table WHERE value = 500")
    cur.fetchall()
    time_with_index = (time.perf_counter() - start) * 1000

    return (round(time_no_index, 3), round(time_with_index, 3))


def task4_join_with_index(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT e.name, d.name, d.location, e.salary
        FROM employees e
        INNER JOIN departments d ON e.dept_id = d.id
        ORDER BY e.salary DESC
    """)
    return cur.fetchall()


if __name__ == "__main__":
    conn = init_db()
    print("=" * 50)
    print("Day 18 — 索引与约束（参考答案）")
    print("=" * 50)

    print("\n[任务1] 约束测试：")
    r1, r2, r3 = task1_constraints(conn)
    print(f"  UNIQUE 冲突: {r1}")
    print(f"  CHECK 冲突:  {r2}")
    print(f"  外键冲突:    {r3}")
    errors = sum(1 for r in [r1, r2, r3] if "成功" not in r)
    assert errors >= 2
    print("  ✅ 通过！")

    print("\n[任务2] EXPLAIN：")
    plan = task2_explain(conn)
    for line in plan:
        print(f"  {line}")
    assert len(plan) > 0
    print("  ✅ 通过！")

    print("\n[任务3] 索引性能对比：")
    no_idx, with_idx = task3_index_performance(conn)
    print(f"  无索引: {no_idx}ms")
    print(f"  有索引: {with_idx}ms")
    if with_idx > 0:
        print(f"  加速比: {no_idx/with_idx:.1f}x")
    print("  ✅ 通过！")

    print("\n[任务4] JOIN查询：")
    result = task4_join_with_index(conn)
    for row in result:
        print(f"  {row[0]} | {row[1]} | {row[2]} | ¥{row[3]}")
    expected = [
        ('赵六', '市场部', '上海', 20000.0), ('李四', '技术部', '杭州', 18000.0),
        ('张三', '技术部', '杭州', 15000.0), ('王五', '市场部', '上海', 12000.0),
    ]
    assert result == expected
    print("  ✅ 通过！")

    conn.close()
    print("\n🎉 全部通过！")
