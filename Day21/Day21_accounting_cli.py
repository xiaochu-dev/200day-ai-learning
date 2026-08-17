"""
Day 21 — 小项目：个人记账 CLI

运行方式：直接运行本文件即可
python Day21_accounting_cli.py

数据库文件：day21_accounting.db（自动创建）
"""

import sqlite3
import os
import csv
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "day21_accounting.db")


# ============================================================
# 初始化数据库
# ============================================================
def init_db():
    """创建表（如果不存在）+ 插入示例数据"""
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                note TEXT
            )
        """)


# ============================================================
# TODO 1：记一笔
# ============================================================
def add_record():
    """
    要求：
    1. 提示用户输入：类型（收入/支出）、金额、分类、日期（YYYY-MM-DD）、备注（可选）
    2. 输入校验：
       - 类型必须是 "income" 或 "expense"（允许用户输入"收入"/"支出"再转换）
       - 金额必须是正数
       - 日期格式必须是 YYYY-MM-DD
    3. 校验通过后 INSERT 到 records 表
    4. 打印 "✅ 已记录！"

    提示：
        type_val = "income" if user_input in ("收入", "income") else "expense"
        amount = float(input("金额："))
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 2：查看本月账单
# ============================================================
def view_this_month():
    """
    要求：
    1. 提供选项：1=全部  2=仅收入  3=仅支出
    2. 查询本月（当前年月）的记录，按日期降序排列
    3. 格式化输出每笔记录，最后打印本月的收入总和、支出总和、结余

    本月判断：date LIKE '2026-08%'（用 datetime.now().strftime("%Y-%m") 获取当前年月）

    输出示例：
    ---- 本月账单 (2026-08) ----
    08-06 | 支出 | 餐饮 | -35.00 | 午饭
    08-05 | 收入 | 工资 | +8000.00 |
    ...
    ---- 合计 ----
    总收入: 8000.00
    总支出: 35.00
    结余: 7965.00

    提示：
        cur.execute("SELECT * FROM records WHERE date LIKE ? ORDER BY date DESC", (this_month + "%",))
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 3：分类统计
# ============================================================
def category_stats():
    """
    要求：
    1. 按 category 和 type 分组统计金额总和
    2. 计算总支出金额，然后计算每个分类占总支出的百分比
    3. 输出格式：

    分类      类型      金额        占比
    ----      ----      ------      ----
    餐饮      支出      500.00      25.0%
    交通      支出      300.00      15.0%
    工资      收入      8000.00     (收入不计算占比)
    ...

    提示：
        cur.execute(
            "SELECT category, type, SUM(amount) as total FROM records "
            "GROUP BY category, type ORDER BY total DESC"
        )
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 4：月度统计
# ============================================================
def monthly_stats():
    """
    要求：
    1. 按月份（如 "2026-08"）和类型分组汇总
    2. 每个月份显示收入总和、支出总和、结余
    3. 按月排序

    输出示例：
    月份        收入         支出         结余
    ----        ----         ----         ----
    2026-07     10000.00     3000.00      7000.00
    2026-08     8000.00      1500.00      6500.00

    提示：
        用 substr(date, 1, 7) 提取年月
        用 SUM(CASE WHEN type='income' THEN amount ELSE 0 END) 分别统计
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# TODO 5：导出 CSV
# ============================================================
def export_csv():
    """
    要求：
    1. 查询所有记录（id, type, amount, category, date, note）
    2. 导出到 day21_records.csv（当前目录）
    3. 包含表头，编码 utf-8-sig
    4. 打印导出的行数和文件路径
    """
    # TODO: 你的代码在这里
    pass


# ============================================================
# 主菜单（不需要修改）
# ============================================================
def main():
    init_db()
    while True:
        print("\n" + "=" * 30)
        print("===== 个人记账 =====")
        print("=" * 30)
        print("1. 记一笔")
        print("2. 查看本月账单")
        print("3. 分类统计")
        print("4. 月度统计")
        print("5. 导出 CSV")
        print("0. 退出")

        choice = input("请选择: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            view_this_month()
        elif choice == "3":
            category_stats()
        elif choice == "4":
            monthly_stats()
        elif choice == "5":
            export_csv()
        elif choice == "0":
            print("再见！")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()
