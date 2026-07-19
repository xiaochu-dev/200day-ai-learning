"""
Day7 — main.py
学生管理系统 CLI 入口

运行：python main.py

⚠️ 本文件是需要你动手填写的练习模板，每个 `# TODO:` 需要补全。
"""

from models import Student, Monitor
from services import StudentManager


def show_menu():
    """显示菜单"""
    print("\n" + "=" * 40)
    print("       学生管理系统 v1.0")
    print("=" * 40)
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 按成绩筛选（生成器）")
    print("4. 删除学生")
    print("5. 统计信息")
    print("6. 退出")
    print("=" * 40)


def add_student_flow(manager):
    """添加学生流程"""
    print("\n--- 添加学生 ---")
    name = input("姓名: ").strip()
    if not name:
        print("❌ 姓名不能为空")
        return

    # TODO 1: 用 try/except 安全获取年龄和成绩
    # - age: int(input(...)), 如果 ValueError 则提示并 return
    # - score: float(input(...)), 同样处理
    # - 调用 manager.add_student(Student(name, age, score))
    # - 打印 "✅ 已添加: {student}"
    try:
        age = int(input("年龄: ").strip())
        score = float(input("成绩: ").strip())
    except ValueError:
        print("❌ 年龄和成绩必须是数字")
        return
    student = Student(name, age, score)
    manager.add_student(student)
    print(f"✅ 已添加: {student}")


def list_students_flow(manager):
    """查看所有学生"""
    print("\n--- 所有学生 ---")
    students = manager.list_all()
    if not students:
        print("（暂无学生）")
        return
    for i,s in enumerate(students, 1):
        print(f"{i}. {s}")
    # TODO 2: 用 enumerate 遍历并打印，格式：
    # 1. 张三, 18岁, 当前成绩: 85
    # 2. 李四, 19岁, 当前成绩: 92, 班长职责: 收作业



def filter_flow(manager):
    """生成器筛选流程"""
    print("\n--- 按成绩筛选 ---")

    # TODO 3: 安全获取最低分，调用 filter_students 生成器
    # - 用生成器逐个 yield 并打印
    # - 如果生成器没有产出任何结果，打印"（没有符合条件的学生）"
    #
    # 提示：手动遍历生成器
    # count = 0
    # for student in manager.filter_students(min_score):
    #     print(student)
    #     count += 1
    # if count == 0: ...
    try:
        min_score = float(input("最低分: ").strip())
    except ValueError:
        print("❌ 请输入数字")
        return
    count=0
    for student in manager.filter_students(min_score):
        print(f"  {student}")
        count += 1
    if count == 0:
        print("(没有符合条件的学生)")
    else:
        print(f"共{count}人成绩 >= {min_score}")

def delete_flow(manager):
    """删除学生流程"""
    print("\n--- 删除学生 ---")
    name = input("要删除的学生姓名: ").strip()
    if not name:
        print("❌ 姓名不能为空")
        return

    # TODO 4: 调用 manager.remove_student(name)
    # - 如果返回 None：打印"❌ 未找到: {name}"
    # - 如果返回学生对象：打印"✅ 已删除: {student}"
    removed = manager.remove_student(name)
    if removed:
        print(f"✅ 已删除: {removed}")
    else:
        print(f"❌ 未找到: {name}")


def stats_flow(manager):
    """统计信息流程"""
    print("\n--- 统计信息 ---")
    # TODO 5: 调用 manager.get_statistics()
    # - 打印每个统计项
    # - 调用 manager.get_top_student() 显示最高分学生
    stats = manager.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    top = manager.get_top_student()
    if top:
        student, score = top
        print(f" 🏆 最高分学生: {student.name} ({score}分)")


# ============================================================
# TODO 6: 主循环
# ============================================================
def main():
    """
    主程序入口

    要求：
    1. 使用 while 循环
    2. 根据用户输入的数字调用对应函数
    3. 用 if/elif 或字典映射（选做：字典映射更优雅）
    4. 输入 '6' 时 break
    5. 捕获 KeyboardInterrupt（Ctrl+C）优雅退出
    """
    manager = StudentManager()
    manager.add_student(Student("张三", 18, 85))
    manager.add_student(Student("李四", 19, 92))
    manager.add_student(Monitor("王五", 18, 78, "组织自习"))
    manager.add_student(Student("赵六", 20, 55))

    actions={
        '1': ('添加学生', add_student_flow),
        '2': ('查看所有学生', list_students_flow),
        '3': ('按成绩筛选', filter_flow),
        '4': ('删除学生', delete_flow),
        '5': ('统计信息', stats_flow),}
    # 预置一些测试数据（写完代码后取消注释测试）
    # manager.add_student(Student("张三", 18, 85))
    # manager.add_student(Student("李四", 19, 92))
    # manager.add_student(Monitor("王五", 18, 78, "组织自习"))
    # manager.add_student(Student("赵六", 20, 55))

    # TODO: 实现主循环
    # while True:
    #     show_menu()
    #     choice = input("请选择 (1-6): ").strip()
    #     if choice == '1': add_student_flow(manager)
    #     elif choice == '2': list_students_flow(manager)
    #     ...

    while True:
        try:
            show_menu()
            choice = input("请选择 (1-6): ").strip()
            if choice == '6':
                print("👋 再见！")
                break
            if choice in actions:
                actions[choice][1](manager)
            else:
                print("❌ 无效选项，请输入 1-6")
        except KeyboardInterrupt:
            print("\\n👋 再见！")
            break
        except ValueError as e:
            print(f"❌ 数据错误: {e}")


if __name__ == "__main__":
    main()

# ============================================================
# 参考答案
# ============================================================
"""
def add_student_flow(manager):
    print("\\n--- 添加学生 ---")
    name = input("姓名: ").strip()
    if not name:
        print("❌ 姓名不能为空")
        return
    try:
        age = int(input("年龄: ").strip())
        score = float(input("成绩: ").strip())
    except ValueError:
        print("❌ 年龄和成绩必须是数字")
        return
    student = Student(name, age, score)
    manager.add_student(student)
    print(f"✅ 已添加: {student}")


def list_students_flow(manager):
    print("\\n--- 所有学生 ---")
    students = manager.list_all()
    if not students:
        print("（暂无学生）")
        return
    for i, s in enumerate(students, 1):
        print(f"{i}. {s}")


def filter_flow(manager):
    print("\\n--- 按成绩筛选 ---")
    try:
        min_score = float(input("最低分: ").strip())
    except ValueError:
        print("❌ 请输入数字")
        return
    count = 0
    for student in manager.filter_students(min_score):
        print(f"  {student}")
        count += 1
    if count == 0:
        print("（没有符合条件的学生）")
    else:
        print(f"共 {count} 人成绩 >= {min_score}")


def delete_flow(manager):
    print("\\n--- 删除学生 ---")
    name = input("要删除的学生姓名: ").strip()
    if not name:
        print("❌ 姓名不能为空")
        return
    removed = manager.remove_student(name)
    if removed:
        print(f"✅ 已删除: {removed}")
    else:
        print(f"❌ 未找到: {name}")


def stats_flow(manager):
    print("\\n--- 统计信息 ---")
    stats = manager.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    top = manager.get_top_student()
    if top:
        student, score = top
        print(f"  🏆 最高分学生: {student.name} ({score}分)")


def main():
    manager = StudentManager()
    manager.add_student(Student("张三", 18, 85))
    manager.add_student(Student("李四", 19, 92))
    manager.add_student(Monitor("王五", 18, 78, "组织自习"))
    manager.add_student(Student("赵六", 20, 55))

    actions = {
        '1': ('添加学生', add_student_flow),
        '2': ('查看所有学生', list_students_flow),
        '3': ('按成绩筛选', filter_flow),
        '4': ('删除学生', delete_flow),
        '5': ('统计信息', stats_flow),
    }

    while True:
        try:
            show_menu()
            choice = input("请选择 (1-6): ").strip()
            if choice == '6':
                print("👋 再见！")
                break
            if choice in actions:
                actions[choice][1](manager)
            else:
                print("❌ 无效选项，请输入 1-6")
        except KeyboardInterrupt:
            print("\\n👋 再见！")
            break
        except ValueError as e:
            print(f"❌ 数据错误: {e}")


if __name__ == "__main__":
    main()
"""
