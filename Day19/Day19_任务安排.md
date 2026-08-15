# Day 19 — Python + SQLite 基础

> Python 操作数据库 + 词汇自测 | 2026-08-04（周一）

---

## 今日目标

1. **Python 开发**：掌握 sqlite3 模块操作 SQLite 数据库，CRUD + 参数化查询
2. **词汇**：Group 6 #1-25（loan ~ tackle），过关线 **20/25**

---

## 任务清单

### AI开发（90min）

- [ ] **阅读概念**：sqlite3 模块、参数化查询为什么防 SQL 注入、fetchone/fetchall/fetchmany
- [ ] **SQLite 练习** — `Day19_python_sqlite.py`（4 个 TODO）
  - [ ] TODO 1：创建数据库和表（用户表），插入初始数据
  - [ ] TODO 2：参数化查询，按城市查询用户
  - [ ] TODO 3：CRUD 完整操作（新增/更新/删除）
  - [ ] TODO 4：结果集转字典列表
- [ ] **运行验证**：`python Day19_python_sqlite.py` 全部通过

### 英语（30min）

- [ ] **词汇自测 25 词** — `Day19_单词自测.txt`（做完发给 Claude 批改）
- [ ] VOA 精听 15 分钟

---

## 核心概念

### sqlite3 模块
```python
import sqlite3

# 连接数据库（文件不存在则自动创建）
conn = sqlite3.connect("mydb.db")

# 推荐用 with 语句管理连接（自动 commit/close）
with sqlite3.connect("mydb.db") as conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE ...")
    # with 结束时自动 conn.commit()
```

### 参数化查询（防 SQL 注入）
```python
# ❌ 危险写法——SQL 注入风险
name = input("输入用户名：")
cur.execute(f"SELECT * FROM users WHERE name = '{name}'")

# ✅ 安全写法——参数化查询
name = input("输入用户名：")
cur.execute("SELECT * FROM users WHERE name = ?", (name,))
```

### 查询方法对比
| 方法 | 返回 | 用法 |
|------|------|------|
| `fetchone()` | 一行 (tuple 或 None) | 查单个用户 |
| `fetchall()` | 所有行 (list of tuple) | 遍历全部结果 |
| `fetchmany(n)` | n 行 (list of tuple) | 分页查询 |

### 用户表结构
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE,
    city TEXT
);
```

测试数据：
| id | name | age | email | city |
|----|------|-----|-------|------|
| 1 | 张三 | 25 | zhangsan@qq.com | 北京 |
| 2 | 李四 | 30 | lisi@qq.com | 上海 |
| 3 | 王五 | 28 | wangwu@qq.com | 北京 |
| 4 | 赵六 | 22 | zhaoliu@qq.com | 广州 |

---

## 收尾

```
cd E:\Users\MyFiles\Desktop\200day
git add Day19/
git commit -m "Day19: Python+SQLite基础 + 词汇 Group6 #1-25"
git push
```
