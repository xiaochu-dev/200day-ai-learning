"""Day 2 单词自测——交互式英译中 quiz"""

WORDS = [
    ("dramatic", "戏剧性的；巨大的；引人注目的"),
    ("eliminate", "消除；淘汰"),
    ("emerge", "出现；浮现；显露"),
    ("emphasis", "强调；重点"),
    ("encounter", "遭遇；遇到"),
    ("enhance", "增强；提高"),
    ("enormous", "巨大的；庞大的"),
    ("equivalent", "等价的；等价物"),
    ("evaluate", "评估；评价"),
    ("eventually", "最终；终于"),
    ("evident", "明显的；显然的"),
    ("exceed", "超过；超越"),
    ("explicit", "明确的；直截了当的"),
    ("exploit", "开发；利用；剥削"),
    ("external", "外部的；外界的"),
    ("facilitate", "促进；使便利"),
    ("flexible", "灵活的；柔韧的"),
    ("fluctuate", "波动；起伏"),
    ("fundamental", "基本的；根本的"),
    ("generate", "产生；生成"),
    ("guarantee", "保证；担保"),
    ("identical", "完全相同的；同一的"),
    ("illustrate", "阐明；举例说明"),
    ("implement", "实施；执行"),
    ("implicit", "含蓄的；隐含的；不明显的"),
    ("inevitable", "不可避免的"),
    ("infrastructure", "基础设施"),
    ("innovation", "创新；革新"),
    ("investigate", "调查；研究"),
    ("justify", "证明……正当；为……辩护"),
]

import random


def run_quiz(words: list[tuple[str, str]]) -> dict:
    """执行一轮单词测试，返回结果"""
    items = words[:]  # 复制一份
    random.shuffle(items)

    correct = []
    wrong = []
    total = len(items)

    print(f"\n{'='*50}")
    print(f"  Day 2 单词自测（共 {total} 题）")
    print(f"  输入中文意思，输入 q 提前退出")
    print(f"{'='*50}\n")

    for i, (en, cn) in enumerate(items, 1):
        print(f"第 {i}/{total} 题：{en}")
        ans = input("你的答案：").strip()

        if ans.lower() == 'q':
            remaining = items[i - 1:]  # 包含当前这题
            print(f"\n已退出，剩余 {len(remaining)} 题未答。")
            break

        if ans == cn:
            print("✅ 正确！\n")
            correct.append((en, cn))
        else:
            print(f"❌ 错误！正确答案：{cn}\n")
            wrong.append((en, cn))

    return {"correct": correct, "wrong": wrong}


def print_result(result: dict, total_words: int):
    """打印测试结果"""
    correct = result["correct"]
    wrong = result["wrong"]
    answered = len(correct) + len(wrong)
    score = len(correct)
    rate = score / answered * 100 if answered > 0 else 0

    print(f"\n{'='*50}")
    print("  测试结果")
    print(f"{'='*50}")
    print(f"  答对：{score} / 已答 {answered}（全部 {total_words} 题）")
    print(f"  正确率：{rate:.1f}%")

    if answered < total_words:
        print(f"  未答：{total_words - answered} 题")

    if rate >= 80 and answered >= total_words:
        print(f"\n  🎉 达标！({rate:.0f}% ≥ 80%)")
    elif answered > 0:
        print(f"\n  ⚠️ 未达标（{rate:.0f}%，需 ≥ 80%），建议复习错词后重测。")

    if wrong:
        print(f"\n  📝 错词清单：")
        for en, cn in wrong:
            print(f"     {en} — {cn}")


def retry_wrong(wrong_words: list[tuple[str, str]]):
    """只补测错词"""
    if not wrong_words:
        print("没有错词，无需补测！")
        return

    input(f"\n按 Enter 开始补测 {len(wrong_words)} 个错词...")
    result = run_quiz(wrong_words)

    # 合并结果显示
    if result["wrong"]:
        print(f"\n  📝 仍然错误：")
        for en, cn in result["wrong"]:
            print(f"     {en} — {cn}")
    else:
        print(f"\n  🎉 错词全部通过！")


def main():
    # 第一轮
    result = run_quiz(WORDS)
    print_result(result, len(WORDS))

    # 如果有错词，问是否补测
    if result["wrong"]:
        print()
        again = input("要补测错词吗？(y/n)：").strip().lower()
        if again == 'y':
            retry_wrong(result["wrong"])

    input("\n按 Enter 退出...")


if __name__ == "__main__":
    main()
