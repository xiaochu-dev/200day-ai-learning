"""
Day 18 — 索引与约束练习

运行方式：直接运行本文件即可
python Day18_sql_index.py
"""

import sqlite3
import time


def init_db():
    """创建带约束的数据库"""
    conn = sqlite3.connect(":memory:")
    # 不使用 row_factory，保持结果为 tuple 便于 assert 比较
    cur = conn.cursor()

    # 创建部门表（有约束）
    cur.execute("""
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            location TEXT DEFAULT '杭州'
        )
    """)

    # 插入部门
    cur.executemany(
        "INSERT INTO departments (id, name, location) VALUES (?, ?, ?)",
        [(1, '技术部', '杭州'), (2, '市场部', '上海'), (3, '人事部', '北京')],
    )

    # 创建员工表（有外键约束）
    # ⚠️ SQLite 需要先开启外键支持
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

    # 插入员工
    employees = [
        (1, '张三', 'zhangsan@qq.com', 15000.0, 1),
        (2, '李四', 'lisi@qq.com', 18000.0, 1),
        (3, '王五', 'wangwu@qq.com', 12000.0, 2),
        (4, '赵六', 'zhaoliu@qq.com', 20000.0, 2),
    ]
    cur.executemany(
        "INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employees
    )
    conn.commit()

    # 创建一张大表用于索引性能对比
    cur.execute("""
        CREATE TABLE big_table (
            id INTEGER PRIMARY KEY,
            name TEXT,
            value INTEGER
        )
    """)
    # 插入 10000 条数据
    for i in range(10000):
        cur.execute(
            "INSERT INTO big_table (name, value) VALUES (?, ?)",
            (f"item_{i}", i % 1000),
        )
    conn.commit()
    return conn


# ============================================================
# TODO 1：创建带约束的表
# ============================================================
def task1_constraints(conn):
    """
    测试各种约束。请补全下面三条 SQL 的预期行为：

    1. 尝试插入重复的 email（zhangsan@qq.com）→ 应该报什么错？
    2. 尝试插入 salary = -500 → 应该报什么错？
    3. 尝试插入 dept_id = 99（不存在的部门）→ 应该报什么错？

    返回三个结果组成的元组 (result1, result2, result3)，
    每个 result 是 "成功" 或错误信息的前20个字符。
    """
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


# ============================================================
# TODO 2：创建索引 + EXPLAIN QUERY PLAN
# ============================================================
def task2_explain(conn):
    """
    1. 在 big_table 的 name 列上创建索引
    2. 用 EXPLAIN QUERY PLAN 分析查询 SELECT * FROM big_table WHERE name = 'item_5000'
    3. 返回 EXPLAIN 输出的文本（前3行）

    提示：EXPLAIN QUERY PLAN 的返回是 rows，取 description 字段即可
    """
    cur = conn.cursor()
    # TODO: 1. 创建索引
    cur.execute("""
        -- 在这里创建索引
    """)

    # TODO: 2. EXPLAIN 分析
    cur.execute("""
        -- 在这里写 EXPLAIN QUERY PLAN
    """)
    plan = cur.fetchall()
    # 转为文本列表
    return [str(row) for row in plan]


# ============================================================
# TODO 3：索引性能对比
# ============================================================
def task3_index_performance(conn):
    """
    对比：有索引 vs 无索引 的查询性能。

    思路：
    1. 先在没有索引的 value 列上查询（SELECT COUNT(*) FROM big_table WHERE value = 500）
       计时
    2. 在 value 列上创建索引
    3. 再次查询同样的条件，计时
    4. 返回 (无索引耗时_ms, 有索引耗时_ms)

    提示：用 time.perf_counter() 计时
    """
    cur = conn.cursor()

    # TODO: 1. 无索引查询计时
    start = time.perf_counter()
    cur.execute("-- 查询 value = 500 的行数")
    cur.fetchall()
    time_no_index = (time.perf_counter() - start) * 1000  # 转毫秒

    # TODO: 2. 创建索引
    cur.execute("-- 创建索引")

    # TODO: 3. 有索引查询计时
    start = time.perf_counter()
    cur.execute("-- 同样的查询")
    cur.fetchall()
    time_with_index = (time.perf_counter() - start) * 1000

    return (round(time_no_index, 3), round(time_with_index, 3))


# ============================================================
# TODO 4：JOIN + 索引
# ============================================================
def task4_join_with_index(conn):
    """
    查询所有员工及其部门名称和地点。

    返回 (employee_name, dept_name, dept_location, salary)，
    按 salary 降序排列。

    提示：用 INNER JOIN（或直接用 employees.dept_id = departments.id）

    预期：
    [('赵六', '市场部', '上海', 20000.0), ('李四', '技术部', '杭州', 18000.0),
     ('张三', '技术部', '杭州', 15000.0), ('王五', '市场部', '上海', 12000.0)]
    """
    cur = conn.cursor()
    # TODO: JOIN 查询
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
    print("Day 18 — 索引与约束练习")
    print("=" * 50)

    print("\n[任务1] 约束测试：")
    r1, r2, r3 = task1_constraints(conn)
    print(f"  UNIQUE 冲突: {r1}")
    print(f"  CHECK 冲突:  {r2}")
    print(f"  外键冲突:    {r3}")
    # 验证至少两个是错误（不是"成功"）
    errors = sum(1 for r in [r1, r2, r3] if "成功" not in r)
    assert errors >= 2, f"❌ 预期至少2个约束报错，实际{errors}个"
    print("  ✅ 通过！")

    print("\n[任务2] EXPLAIN QUERY PLAN：")
    plan = task2_explain(conn)
    for line in plan:
        print(f"  {line}")
    assert len(plan) > 0, "❌ EXPLAIN 没有输出"
    print("  ✅ 通过！")

    print("\n[任务3] 索引性能对比：")
    no_idx, with_idx = task3_index_performance(conn)
    print(f"  无索引: {no_idx}ms")
    print(f"  有索引: {with_idx}ms")
    print(f"  加速比: {no_idx/with_idx:.1f}x" if with_idx > 0 else "  (无数据)")
    # 不做严格断言（结果可大可小），但至少两个值都应该有
    assert no_idx >= 0 and with_idx >= 0, "❌ 计时结果异常"
    print("  ✅ 通过！")

    print("\n[任务4] JOIN查询员工+部门：")
    result = task4_join_with_index(conn)
    for row in result:
        print(f"  {row[0]} | {row[1]} | {row[2]} | ¥{row[3]}")
    expected = [
        ('赵六', '市场部', '上海', 20000.0), ('李四', '技术部', '杭州', 18000.0),
        ('张三', '技术部', '杭州', 15000.0), ('王五', '市场部', '上海', 12000.0),
    ]
    assert result == expected, f"❌ 不通过！\n期望: {expected}\n实际: {result}"
    print("  ✅ 通过！")

    conn.close()
    print("\n🎉 全部通过！Day 18 索引与约束完成！")
