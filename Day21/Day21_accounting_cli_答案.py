"""
Day 21 — 小项目：个人记账 CLI（参考答案）

运行方式：直接运行本文件即可
python Day21_accounting_cli_答案.py

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
# 记一笔
# ============================================================
def add_record():
    print("\n--- 记一笔 ---")

    # 类型输入
    t = input("类型（收入/支出）: ").strip()
    if t in ("收入", "income"):
        type_val = "income"
    elif t in ("支出", "expense"):
        type_val = "expense"
    else:
        print("❌ 类型无效，请输入「收入」或「支出」")
        return

    # 金额输入
    try:
        amount = float(input("金额: ").strip())
        if amount <= 0:
            print("❌ 金额必须大于 0")
            return
    except ValueError:
        print("❌ 金额格式错误")
        return

    # 分类输入
    category = input("分类（如 餐饮/交通/工资）: ").strip()
    if not category:
        print("❌ 分类不能为空")
        return

    # 日期输入
    date_str = input("日期（YYYY-MM-DD，回车=今天）: ").strip()
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        # 简单校验格式
        parts = date_str.split("-")
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            print("❌ 日期格式错误，应为 YYYY-MM-DD")
            return

    # 备注（可选）
    note = input("备注（可选，回车跳过）: ").strip()

    # 写入数据库
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO records (type, amount, category, date, note) VALUES (?, ?, ?, ?, ?)",
            (type_val, amount, category, date_str, note if note else None)
        )
        print("✅ 已记录！")


# ============================================================
# 查看本月账单
# ============================================================
def view_this_month():
    print("\n选项：1=全部  2=仅收入  3=仅支出")
    sub = input("请选择（默认1）: ").strip() or "1"

    this_month = datetime.now().strftime("%Y-%m")

    if sub == "2":
        type_filter = "AND type = 'income'"
        title = f"本月账单 ({this_month}) — 仅收入"
    elif sub == "3":
        type_filter = "AND type = 'expense'"
        title = f"本月账单 ({this_month}) — 仅支出"
    else:
        type_filter = ""
        title = f"本月账单 ({this_month}) — 全部"

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            f"SELECT date, type, category, amount, note FROM records "
            f"WHERE date LIKE ? {type_filter} ORDER BY date DESC",
            (this_month + "%",)
        )
        rows = cur.fetchall()

    if not rows:
        print("暂无记录。")
        return

    total_income = 0.0
    total_expense = 0.0

    print(f"\n---- {title} ----")
    for row in rows:
        date_str, t, cat, amt, note = row
        if t == "income":
            sign = "+"
            total_income += amt
        else:
            sign = "-"
            total_expense += amt
        note_str = note if note else ""
        # 只显示月-日
        short_date = date_str[5:] if len(date_str) >= 10 else date_str
        print(f"{short_date} | {'收入' if t == 'income' else '支出'} | {cat} | {sign}{amt:.2f} | {note_str}")

    print(f"\n---- 合计 ----")
    print(f"总收入: {total_income:.2f}")
    print(f"总支出: {total_expense:.2f}")
    print(f"结余: {total_income - total_expense:.2f}")


# ============================================================
# 分类统计
# ============================================================
def category_stats():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT category, type, SUM(amount) as total "
            "FROM records GROUP BY category, type ORDER BY total DESC"
        )
        rows = cur.fetchall()

        # 计算总支出（用于算占比）
        cur.execute("SELECT SUM(amount) FROM records WHERE type = 'expense'")
        total_expense = cur.fetchone()[0] or 0

    if not rows:
        print("暂无记录。")
        return

    print(f"\n{'分类':<10} {'类型':<8} {'金额':<12} {'占比' if total_expense > 0 else ''}")
    print("-" * 40)
    for cat, t, total in rows:
        type_cn = "收入" if t == "income" else "支出"
        pct = ""
        if t == "expense" and total_expense > 0:
            pct = f"{total / total_expense * 100:.1f}%"
        print(f"{cat:<10} {type_cn:<8} {total:<12.2f} {pct}")


# ============================================================
# 月度统计
# ============================================================
def monthly_stats():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT substr(date, 1, 7) as month, "
            "SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) as income, "
            "SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) as expense "
            "FROM records GROUP BY month ORDER BY month"
        )
        rows = cur.fetchall()

    if not rows:
        print("暂无记录。")
        return

    print(f"\n{'月份':<12} {'收入':<12} {'支出':<12} {'结余':<12}")
    print("-" * 48)
    for month, income, expense in rows:
        balance = income - expense
        print(f"{month:<12} {income:<12.2f} {expense:<12.2f} {balance:<12.2f}")


# ============================================================
# 导出 CSV
# ============================================================
def export_csv():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, type, amount, category, date, note FROM records ORDER BY date")
        rows = cur.fetchall()

    output_path = os.path.join(os.path.dirname(__file__), "day21_records.csv")

    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "type", "amount", "category", "date", "note"])
        writer.writerows(rows)

    print(f"✅ 已导出 {len(rows)} 行数据到 {output_path}")


# ============================================================
# 主菜单
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
