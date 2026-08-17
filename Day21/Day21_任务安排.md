# Day 21 — 小项目：个人记账 CLI

> CLI 应用实战 + 词汇自测 | 2026-08-06（周三）

---

## 今日目标

1. **Python 开发**：综合运用 SQLite + 输入输出 + 循环菜单，完成一个命令行记账程序
2. **词汇**：Group 7 #1-25（habitat ~ devote），过关线 **20/25**

---

## 任务清单

### AI开发（120min）——今日项目较大

- [ ] **阅读概念**：CLI 菜单循环、SQLite 数据聚合（GROUP BY/SUM）、日期处理
- [ ] **记账 CLI 开发** — `Day21_accounting_cli.py`（5 个功能 TODO）
  - [ ] TODO 1：记一笔（收入/支出、金额、分类、日期、备注）
  - [ ] TODO 2：查看本月账单（全部/仅收入/仅支出）
  - [ ] TODO 3：分类统计（按分类汇总金额和占比）
  - [ ] TODO 4：月度统计（按月汇总收入、支出、结余）
  - [ ] TODO 5：导出 CSV
- [ ] **运行验证**：程序启动正常，5 项功能均可使用

### 英语（30min）

- [ ] **词汇自测 25 词** — `Day21_单词自测.txt`（做完发给 Claude 批改）
- [ ] VOA 精听 15 分钟

---

## 核心概念

### 数据库设计

```sql
CREATE TABLE records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,       -- 'income' 或 'expense'
    amount REAL NOT NULL,      -- 金额（正数）
    category TEXT NOT NULL,    -- 分类：餐饮/交通/工资/...
    date TEXT NOT NULL,        -- 日期 YYYY-MM-DD
    note TEXT                  -- 备注（可选）
);
```

### 菜单结构
```
===== 个人记账 =====
1. 记一笔
2. 查看本月账单
3. 分类统计
4. 月度统计
5. 导出 CSV
0. 退出
请选择：
```

### 关键 SQL

```sql
-- 本月账单（2026-08）
SELECT * FROM records WHERE date LIKE '2026-08%' ORDER BY date DESC;

-- 分类统计
SELECT category, type, SUM(amount) as total
FROM records GROUP BY category, type ORDER BY total DESC;

-- 月度统计
SELECT substr(date, 1, 7) as month, type, SUM(amount) as total
FROM records GROUP BY month, type ORDER BY month;
```

### 日期处理
```python
from datetime import datetime
today = datetime.now()
this_month = today.strftime("%Y-%m")  # '2026-08'
```

---

## 收尾

```
cd E:\Users\MyFiles\Desktop\200day
git add Day21/
git commit -m "Day21: 个人记账CLI项目 + 词汇 Group7 #1-25"
git push
```
