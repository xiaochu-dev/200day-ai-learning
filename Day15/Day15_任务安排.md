# Day 15 — SQL基础：数据查询

> 数据库入门 + 词汇自测 | 2026-08-04（周日）

---

## 今日目标

1. **数据库**：理解关系型数据库概念，掌握 SELECT/WHERE/ORDER BY/LIMIT
2. **词汇**：Group 4 #1-25（profit ~ instance），过关线 **20/25**

---

## 任务清单

### AI开发（90min）

- [ ] **阅读概念**：什么是数据库？什么是SQL？SQLite与其他数据库的区别
- [ ] **SQL基础语法练习** — `Day15_sql_basics.py`（4个函数 TODO，用 sqlite3 在内存中操作）
  - [ ] 创建表结构（CREATE TABLE）
  - [ ] WHERE 条件筛选（=, >, <, !=, LIKE, IN, BETWEEN）
  - [ ] ORDER BY 排序（ASC/DESC，多字段排序）
  - [ ] LIMIT 分页（LIMIT + OFFSET）
- [ ] **运行验证**：所有函数输出正确结果

### 英语（30min）

- [ ] **词汇自测 25 词** — `Day15_单词自测.txt`（做完发给 Claude 批改）
- [ ] VOA 精听 15 分钟

---

## 核心概念

### 关系型数据库
- 数据以**表（Table）**的形式组织，一行 = 一条记录，一列 = 一个字段
- 用 **SQL**（Structured Query Language）操作数据
- SQLite：轻量级数据库，整个数据库就是一个文件，不需要安装服务器

### SELECT 查询结构
```sql
SELECT 列名1, 列名2        -- 选哪些列（* = 全部）
FROM 表名                  -- 从哪张表查
WHERE 条件                 -- 筛选哪些行
ORDER BY 列名 ASC/DESC     -- 排序
LIMIT 数量 OFFSET 偏移;    -- 分页
```

### 常用 WHERE 条件
| 条件 | 示例 | 含义 |
|------|------|------|
| = | `grade = 'A'` | 等于 |
| > / < / >= / <= | `score > 80` | 比较 |
| != 或 <> | `dept != 'HR'` | 不等于 |
| LIKE | `name LIKE '张%'` | 模糊匹配（% = 任意字符） |
| IN | `city IN ('杭州','上海')` | 在列表中 |
| BETWEEN | `age BETWEEN 18 AND 25` | 在范围内 |
| AND / OR | `score>80 AND grade='A'` | 组合条件 |

---

## 收尾

```
cd E:\Users\MyFiles\Desktop\200day
git add Day15/
git commit -m "Day15: SQL基础查询 + 词汇 Group4 #1-25"
git push
```
