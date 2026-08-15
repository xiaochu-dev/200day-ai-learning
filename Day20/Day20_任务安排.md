# Day 20 — Python 数据库操作进阶

> 事务/批量/DAO模式/CSV导出 + 词汇自测 | 2026-08-05（周二）

---

## 今日目标

1. **Python 开发**：掌握事务回滚、executemany 批量操作、UserDAO 封装模式、CSV 导出
2. **词汇**：Group 6 #26-50（consult ~ proportion），过关线 **20/25**

---

## 任务清单

### AI开发（90min）

- [ ] **阅读概念**：事务 ACID、executemany vs 逐条 insert、DAO 设计模式、连接池概念
- [ ] **SQLite 进阶练习** — `Day20_python_sqlite_adv.py`（4 个 TODO）
  - [ ] TODO 1：事务操作——转账（两个 UPDATE，失败回滚）
  - [ ] TODO 2：批量插入 1000 条 + execumany vs 逐条性能对比
  - [ ] TODO 3：封装 UserDAO 类（CRUD + find_by_city）
  - [ ] TODO 4：查询结果导出 CSV 文件
- [ ] **运行验证**：`python Day20_python_sqlite_adv.py` 全部通过

### 英语（30min）

- [ ] **词汇自测 25 词** — `Day20_单词自测.txt`（做完发给 Claude 批改）
- [ ] VOA 精听 15 分钟

---

## 核心概念

### 事务（Transaction）

事务是一组操作，要么全部成功，要么全部回滚（原子性）。

```python
conn = sqlite3.connect("bank.db")
try:
    # 转出
    cur.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    # 转入
    cur.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    conn.commit()  # 全部成功，提交
except Exception:
    conn.rollback()  # 任一失败，回滚
```

### executemany vs 逐条 insert

```python
# ❌ 慢：逐条插入 1000 次 commit
for item in data:
    cur.execute("INSERT INTO t VALUES (?)", (item,))
conn.commit()

# ✅ 快：一条语句，一次执行
cur.executemany("INSERT INTO t VALUES (?)", [(item,) for item in data])
conn.commit()
```

**为什么快？** executemany 是一条 SQL 语句重复执行，减少了解析开销和事务开销。

### DAO 模式（Data Access Object）

将数据库操作封装在一个类中，业务代码不直接写 SQL：

```python
class UserDAO:
    def __init__(self, db_path):
        self.db_path = db_path

    def create(self, name, age, email, city): ...
    def find_by_id(self, user_id): ...
    def update(self, user_id, **kwargs): ...
    def delete(self, user_id): ...
    def find_by_city(self, city): ...
```

### CSV 导出

```python
import csv

rows = cur.fetchall()
with open("users.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "age", "email", "city"])  # 表头
    writer.writerows(rows)  # 数据
```

> **连接池概念**：Web 应用中不会每次都创建新连接，而是维护一个连接池（connection pool），
> 需要时从池中借，用完归还。Python 常用 `sqlalchemy` 实现。本次练习暂用简单连接方式。

---

## 收尾

```
cd E:\Users\MyFiles\Desktop\200day
git add Day20/
git commit -m "Day20: SQLite进阶(事务/批量/DAO/CSV) + 词汇 Group6 #26-50"
git push
```
