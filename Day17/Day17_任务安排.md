# Day 17 — 多表操作：JOIN + GROUP BY + 子查询

> 数据库关联查询 + 词汇自测 | 2026-08-06（周二）

---

## 今日目标

1. **数据库**：掌握多表 JOIN、GROUP BY + HAVING、子查询
2. **词汇**：Group 5 #1-25（yield ~ domestic），过关线 **20/25**

---

## 任务清单

### AI开发（90min）

- [ ] **阅读概念**：JOIN 类型、子查询 vs JOIN、HAVING 用法
- [ ] **SQL 多表练习** — `Day17_sql_join.py`（4个函数 TODO）
  - [ ] INNER JOIN 内连接
  - [ ] LEFT JOIN 左连接
  - [ ] GROUP BY + HAVING 分组筛选
  - [ ] 子查询（WHERE 中的子查询）
- [ ] **运行验证**：所有函数输出正确结果

### 英语（30min）

- [ ] **词汇自测 25 词** — `Day17_单词自测.txt`（做完发给 Claude 批改）
- [ ] VOA 精听 15 分钟

---

## 核心概念

### JOIN 类型
```
INNER JOIN    — 两表都匹配的行才返回（交集）
LEFT JOIN     — 左表全部保留，右表无匹配填 NULL
```

### 图解
```
 students                scores
┌────┬──────┐           ┌────┬───────┐
│ id │ name │           │ id │ score │
├────┼──────┤           ├────┼───────┤
│ 1  │ 张三 │───────────│ 1  │  92   │  ← 匹配
│ 2  │ 李四 │──┐  ┌─────│ 2  │  78   │  ← 匹配
│ 3  │ 王五 │  │  │     └────┴───────┘
└────┴──────┘  │  │
    LEFT: 张三(92), 李四(78), 王五(NULL)
    INNER: 张三(92), 李四(78)
```

### 子查询
```sql
-- 查询分数高于平均分的学生
SELECT name, score FROM students
WHERE score > (SELECT AVG(score) FROM students);

-- 查询有订单的用户（用 IN）
SELECT name FROM users
WHERE id IN (SELECT DISTINCT user_id FROM orders);
```

---

## 收尾

```
cd E:\Users\MyFiles\Desktop\200day
git add Day17/
git commit -m "Day17: SQL多表JOIN+子查询 + 词汇 Group5 #1-25"
git push
```
