"""
Day7 — services.py
StudentManager 业务逻辑 + 生成器筛选

⚠️ 本文件是需要你动手填写的练习模板，每个 `# TODO:` 需要补全。
"""

from models import Student, Monitor
from utils import log_call, write_log


# ============================================================
# TODO 1: StudentManager 类
# ============================================================
class StudentManager:
    """学生管理器 —— 增删查改 + 统计"""

    def __init__(self):
        # TODO: 初始化空列表 self.students = []
        self.students = []

    @log_call
    def add_student(self, student):
        """
        添加学生

        要求：
        - 接受 Student 或其子类（Monitor）对象
        - 用 isinstance 检查：如果不是 Student 实例则 raise TypeError
        """
        # TODO: 实现添加逻辑（含类型检查）
        if not isinstance(student, Student):
            raise TypeError(f"必须是 Student 或子类，收到: {type(student)}")
        self.students.append(student)
        write_log(f"添加学生: {student}")

    def list_all(self):
        """
        返回所有学生对象的列表

        提示：for s in self.students: yield s  也可以，但这里直接返回列表
        """
        # TODO: 返回 self.students 的副本
        return self.students.copy()

    def filter_students(self, min_score=0):
        """
        TODO 2: 生成器 —— 逐个 yield 成绩 >= min_score 的学生

        使用 yield 而不是 return 列表！
        这样调用方可以逐个处理，不一次性加载全部数据。

        用法示例：
            for student in manager.filter_students(60):
                print(student)
        """
        # TODO: 实现生成器
        for s in self.students:
            if s.score >= min_score:
                yield s

    def remove_student(self, name):
        """
        按姓名删除学生

        要求：
        - 找到第一个匹配的学生并删除
        - 返回被删除的学生对象
        - 如果没找到，返回 None
        """
        # TODO: 实现删除逻辑
        for i, s in enumerate(self.students):
            if s.name == name:
                removed = self.students.pop(i)
                write_log(f"删除学生: {removed}")
                return removed
        return None

    def get_statistics(self):
        """
        TODO 3: 统计信息

        返回字典：
        {
            "总人数": ...,
            "平均分": ...,
            "最高分": ...,   # 用 max() 内置函数
            "最低分": ...,   # 用 min() 内置函数
            "及格人数": ...,
        }

        提示：
        - 用列表推导式收集所有成绩：[s.score for s in self.students]
        - 平均分用 sum() / len()
        - 最高/最低用 max() / min()
        """
        # TODO: 实现统计
        if not self.students:
            return {"总人数":0,"平均分":0,"最高分":0,"最低分":0,"及格人数":0}
        scores = [s.score for s in self.students]
        return {
            "总人数": len(self.students),
            "平均分": round(sum(scores) / len(scores), 1),
            "最高分": max(scores),
            "最低分": min(scores),
            "及格人数": sum(1 for s in scores if s >= 60),
        }

    @log_call
    def get_top_student(self):
        """
        TODO 4: 找最高分学生

        返回: (Student对象, 分数)

        提示：用 max() 函数的 key 参数
        max(self.students, key=lambda s: s.score)
        """
        # TODO: 实现
        if not self.students:
            return None
        top = max(self.students, key=lambda s: s.score)
        return (top, top.score)


# ============================================================
# 参考答案
# ============================================================
"""
class StudentManager:
    def __init__(self):
        self.students = []

    @log_call
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError(f"必须是 Student 或子类，收到: {type(student)}")
        self.students.append(student)
        write_log(f"添加学生: {student}")

    def list_all(self):
        return self.students.copy()

    def filter_students(self, min_score=0):
        for s in self.students:
            if s.score >= min_score:
                yield s

    def remove_student(self, name):
        for i, s in enumerate(self.students):
            if s.name == name:
                removed = self.students.pop(i)
                write_log(f"删除学生: {removed}")
                return removed
        return None

    def get_statistics(self):
        if not self.students:
            return {"总人数": 0, "平均分": 0, "最高分": 0, "最低分": 0, "及格人数": 0}
        scores = [s.score for s in self.students]
        return {
            "总人数": len(self.students),
            "平均分": round(sum(scores) / len(scores), 1),
            "最高分": max(scores),
            "最低分": min(scores),
            "及格人数": sum(1 for s in scores if s >= 60),
        }

    @log_call
    def get_top_student(self):
        if not self.students:
            return None
        top = max(self.students, key=lambda s: s.score)
        return (top, top.score)
"""
