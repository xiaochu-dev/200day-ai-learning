# Day 18 — 索引与约束

> 数据库性能优化 + 词汇自测 | 2026-08-07（周三）

---

## 今日目标

1. **数据库**：理解主键/外键/唯一约束/索引，会用 EXPLAIN 查看查询计划
2. **词汇**：Group 5 #26-50（ongoing ~ regardless of），过关线 **20/25**

---

## 任务清单

### AI开发（90min）

- [ ] **阅读概念**：约束类型、索引原理（B-Tree）、查询计划 EXPLAIN
- [ ] **索引与约束练习** — `Day18_sql_index.py`（4个函数 TODO）
  - [ ] 创建带约束的表（PK/FK/UNIQUE/NOT NULL/DEFAULT）
  - [ ] 创建索引 + 对比查询性能
  - [ ] EXPLAIN QUERY PLAN 分析
  - [ ] 外键约束验证
- [ ] **运行验证**：所有函数输出正确结果

### 英语（30min）

- [ ] **词汇自测 25 词** — `Day18_单词自测.txt`（做完发给 Claude 批改）
- [ ] VOA 精听 15 分钟

---

## 核心概念

### 约束类型
| 约束 | 含义 | 示例 |
|------|------|------|
| PRIMARY KEY | 主键，唯一且非空 | `id INTEGER PRIMARY KEY` |
| FOREIGN KEY | 外键，引用另一张表 | `FOREIGN KEY (uid) REFERENCES users(id)` |
| UNIQUE | 值不能重复 | `email TEXT UNIQUE` |
| NOT NULL | 不能为空 | `name TEXT NOT NULL` |
| DEFAULT | 默认值 | `score REAL DEFAULT 0` |
| CHECK | 自定义检查 | `CHECK (age >= 0 AND age <= 150)` |

### 索引
```sql
-- 创建索引（加快查询速度，但会减慢写入）
CREATE INDEX idx_name ON students(name);
CREATE INDEX idx_city_score ON students(city, score);  -- 复合索引

-- 查看查询计划
EXPLAIN QUERY PLAN SELECT * FROM students WHERE name = '张三';
```

> **索引原理**：类似书的目录。没有索引 = 从头翻到尾（全表扫描）。有索引 = 通过目录直接定位（B-Tree 查找）。

---

## 收尾

```
cd E:\Users\MyFiles\Desktop\200day
git add Day18/
git commit -m "Day18: 索引与约束 + 词汇 Group5 #26-50"
git push
```
