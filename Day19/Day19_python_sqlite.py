"""
Day 19 — Python + SQLite 基础练习

运行方式：直接运行本文件即可
python Day19_python_sqlite.py
"""

import sqlite3
import os

# 数据库文件路径（放在当前目录，不污染项目根目录）
DB_PATH = os.path.join(os.path.dirname(__file__), "day19_test.db")

# ============================================================
# 初始化：清空旧数据库（不影响你的 TODO）
# ============================================================
def cleanup():
    """如果存在旧数据库则删除，确保每次运行干净启动"""
    try:
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
    except PermissionError:
        pass  # Windows 文件锁定延迟，忽略

# ============================================================
# TODO 1：创建数据库和表，插入初始数据
# ============================================================
def task1_create_and_insert():
    """
    要求：
    1. 用 with sqlite3.connect(DB_PATH) 管理连接
    2. 创建 users 表（字段：id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL, age INTEGER, email TEXT UNIQUE, city TEXT）
    3. 用 executemany 插入以下 4 条初始数据：
       (1, '张三', 25, 'zhangsan@qq.com', '北京')
       (2, '李四', 30, 'lisi@qq.com', '上海')
       (3, '王五', 28, 'wangwu@qq.com', '北京')
       (4, '赵六', 22, 'zhaoliu@qq.com', '广州')

    返回：无（创建文件 DB_PATH 即可）
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 2：参数化查询——按城市查询用户
# ============================================================
def task2_query_by_city(city: str):
    """
    要求：
    1. 使用参数化查询（? 占位符）防止 SQL 注入
    2. 查询 users 表中 city 字段匹配的行
    3. 用 fetchall() 返回所有匹配用户

    参数：
        city: 城市名，如 "北京"

    返回：
        list of tuple，如 [('张三', 25, 'zhangsan@qq.com', '北京'), ...]

    提示：SELECT name, age, email, city FROM users WHERE city = ?
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 3：CRUD 完整操作
# ============================================================
def task3_crud():
    """
    要求：依次执行以下操作，全部在同一个 with 块中完成

    1. CREATE：插入新用户 ("孙七", 26, "sunqi@qq.com", "深圳")
    2. READ：用 fetchone() 查出刚插入的孙七，验证插入成功
    3. UPDATE：把孙七的年龄从 26 改成 27
    4. DELETE：删除赵六（id=4）

    返回：
        元组 (new_user, updated_user)
        - new_user: 步骤2查到的孙七记录（插入后的 tuple）
        - updated_user: 步骤3更新后重新查到的孙七记录（更新后的 tuple）

    提示：
        INSERT 后可以用 cur.lastrowid 获取新插入行的 id
        修改 user 表不需要外键约束，INSERT 时 id 用 NULL 让它自增
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 4：查询结果转字典列表
# ============================================================
def task4_to_dict_list():
    """
    要求：
    1. 查询所有用户
    2. 使用 cur.description 获取列名
    3. 将 fetchall() 的结果转成字典列表

    返回：
        list of dict，如：
        [
            {"id": 1, "name": "张三", "age": 25, "email": "zhangsan@qq.com", "city": "北京"},
            ...
        ]

    提示：
        columns = [desc[0] for desc in cur.description]
        dict(zip(columns, row))
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# 测试运行（不需要修改）
# ============================================================
if __name__ == "__main__":
    cleanup()

    print("=" * 50)
    print("Day 19 — Python + SQLite 基础练习")
    print("=" * 50)

    # 任务1
    print("\n[任务1] 创建数据库和表...")
    task1_create_and_insert()
    assert os.path.exists(DB_PATH), "❌ 数据库文件未创建！"
    # 验证表和数据
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
    assert new_user is not None, "❌ 插入失败，未查到孙七"
    assert new_user[1] == "孙七", f"❌ 期望孙七，实际 {new_user[1]}"
    print(f"  插入: {new_user}")
    assert updated_user[2] == 27, f"❌ 期望年龄 27，实际 {updated_user[2]}"
    print(f"  更新后: {updated_user}")
    # 验证赵六已删除
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

    # 清理
    cleanup()
    print("\n🎉 全部通过！Day 19 Python + SQLite 基础完成！")
