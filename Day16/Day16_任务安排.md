# Day 16 — SQL进阶：数据增删改 + 聚合函数

> 数据库操作 + 词汇自测 | 2026-08-05（周一）

---

## 今日目标

1. **数据库**：掌握 INSERT/UPDATE/DELETE，聚合函数 COUNT/SUM/AVG/MAX/MIN
2. **词汇**：Group 4 #26-50（identity ~ imply），过关线 **20/25**

---

## 任务清单

### AI开发（90min）

- [ ] **阅读概念**：数据增删改语法、聚合函数、NULL 处理
- [ ] **SQL 操作练习** — `Day16_sql_crud.py`（4个函数 TODO）
  - [ ] INSERT 插入数据（单条 + 批量）
  - [ ] UPDATE 更新数据（条件更新）
  - [ ] DELETE 删除数据（安全删除）
  - [ ] 聚合函数（COUNT/SUM/AVG/MAX/MIN + GROUP BY）
- [ ] **运行验证**：所有函数输出正确结果

### 英语（30min）

- [ ] **词汇自测 25 词** — `Day16_单词自测.txt`（做完发给 Claude 批改）
- [ ] VOA 精听 15 分钟

---

## 核心概念

### INSERT — 插入数据
```sql
-- 单条插入
INSERT INTO students (name, age, score) VALUES ('新同学', 20, 85.5);

-- 批量插入
INSERT INTO students (name, age, score) VALUES
    ('A', 18, 90), ('B', 19, 88), ('C', 20, 92);
```

### UPDATE — 更新数据
```sql
-- ⚠️ 一定要加 WHERE！不加 WHERE 会更新所有行！
UPDATE students SET score = 95 WHERE id = 1;
UPDATE students SET grade = 'A', score = 90 WHERE name = '张三';
```

### DELETE — 删除数据
```sql
-- ⚠️ 一定要加 WHERE！不加 WHERE 会删除所有行！
DELETE FROM students WHERE id = 10;
```

### 聚合函数
| 函数 | 含义 | 示例 |
|------|------|------|
| COUNT(*) | 统计行数 | `SELECT COUNT(*) FROM students` |
| COUNT(列) | 统计非NULL值 | `SELECT COUNT(score) FROM students` |
| SUM(列) | 求和 | `SELECT SUM(score) FROM students` |
| AVG(列) | 平均值 | `SELECT AVG(score) FROM students` |
| MAX(列) | 最大值 | `SELECT MAX(score) FROM students` |
| MIN(列) | 最小值 | `SELECT MIN(score) FROM students` |

### GROUP BY — 分组统计
```sql
-- 按城市统计每个城市的平均分
SELECT city, AVG(score) as avg_score, COUNT(*) as cnt
FROM students
GROUP BY city;

-- 分组后筛选用 HAVING（不能用 WHERE）
SELECT city, AVG(score) as avg_score
FROM students
GROUP BY city
HAVING avg_score >= 80;
```

> **WHERE vs HAVING**：WHERE 在分组前过滤行，HAVING 在分组后过滤组。

---

## 收尾

```
cd E:\Users\MyFiles\Desktop\200day
git add Day16/
git commit -m "Day16: SQL增删改+聚合函数 + 词汇 Group4 #26-50"
git push
```
