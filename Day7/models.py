"""
Day7 — models.py
Person → Student → Monitor 三级继承 + @property 成绩校验

⚠️ 本文件是需要你动手填写的练习模板，不是完整代码！
   每个标记 `# TODO:` 的地方需要你补全。
   参考答案在文件末尾的注释区域。
"""

from utils import log_call


# ============================================================
# TODO 1: Person 基类
# ============================================================
class Person:
    """人 —— 所有角色的基类"""

    def __init__(self, name, age):
        # TODO: 保存 name 和 age 到实例属性
        self.name = name
        self.age = age

    def __str__(self):
        # TODO: 返回 f"{self.name}, {self.age}岁"
        return f"{self.name}, {self.age}岁"


# ============================================================
# TODO 2: Student 类（继承 Person）
# ============================================================
class Student(Person):
    """
    学生 —— 继承 Person，增加成绩管理

    要求：
    - 用 super().__init__() 调用父类
    - 用 @property 做成绩校验（0-100 范围）
    - 用 __scores（私有属性）存历史成绩列表
    """

    def __init__(self, name, age, score=0):
        # TODO: 调用父类 __init__，然后初始化 __scores 列表
        super().__init__(name, age)
        self.__scores = []
        self._score = score

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def score(self, value):
        if not 0 <= value <= 100:
            raise ValueError(f"成绩必须在0-100之间，收到: {value}")
        self._score = value
        self.__scores.append(value)

    # TODO: @property —— 获取 _score
    # TODO: @score.setter —— 校验 0 <= score <= 100，否则 raise ValueError
    #        每次设置成绩时，自动 append 到 __scores

    def add_score(self, score):
        """添加一次考试成绩"""
        # TODO: 利用 self.score setter 来自动存入 __scores
        self.score = score

    def get_score_history(self):
        """返回历史成绩列表的副本（不要暴露原始列表！）"""
        # TODO: 返回 __scores 的副本
        return self.__scores.copy()

    def __str__(self):
        # TODO: 返回 f"{self.name}, {self.age}岁, 当前成绩: {self._score}"
        return f"{self.name}, {self.age}岁, 当前成绩: {self._score}"


# ============================================================
# TODO 3: Monitor 类（继承 Student）
# ============================================================
class Monitor(Student):
    """
    班长 —— 继承 Student，增加职责管理

    要求：
    - 用 super().__init__() 调用父类
    - 重写 __str__()，额外显示职责
    - 新增 manage() 方法
    """

    def __init__(self, name, age, score, duty="收作业"):
        # TODO: 调用父类 __init__，然后保存 duty
        super().__init__(name, age, score)
        self.duty = duty

    def __str__(self):
        return f"{super().__str__()},班长职责: {self.duty}"

    # TODO: 重写 __str__()，显示"班长"身份和职责
    #       格式：张三, 18岁, 当前成绩: 85, 班长职责: 收作业

    @log_call
    def manage(self):
        """班长执行职责"""
        return f"[{self.name}] 正在{self.duty}..."


# ============================================================
# 参考答案（写完后对照）
# ============================================================
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}岁"


class Student(Person):
    def __init__(self, name, age, score=0):
        super().__init__(name, age)
        self.__scores = []
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not 0 <= value <= 100:
            raise ValueError(f"成绩必须在0-100之间，收到: {value}")
        self._score = value
        self.__scores.append(value)

    def add_score(self, score):
        self.score = score  # 触发 setter

    def get_score_history(self):
        return self.__scores.copy()

    def __str__(self):
        return f"{self.name}, {self.age}岁, 当前成绩: {self._score}"


class Monitor(Student):
    def __init__(self, name, age, score, duty="收作业"):
        super().__init__(name, age, score)
        self.duty = duty

    def __str__(self):
        return f"{super().__str__()}, 班长职责: {self.duty}"

    @log_call
    def manage(self):
        return f"[{self.name}] 正在{self.duty}..."
"""
