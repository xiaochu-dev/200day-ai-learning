# Day 7 — Week 2 收官：学生管理系统

> **目标**：综合 Week 2 全部知识点（类/继承/多态/装饰器/生成器/模块），写出一个多文件的 CLI 程序
> **时间**：约 90min Python + 30min 英语

---

## 一、项目：学生管理系统 CLI

### 功能需求

```
1. 添加学生（姓名、年龄、成绩）
2. 查看所有学生
3. 按条件筛选（成绩 >= 某分数）
4. 删除学生
5. 统计（平均分、最高分、最低分）
6. 退出
```

### 文件结构（4 个模块）

```
Day7/
├── models.py      ← 数据模型：Person → Student → Monitor
├── services.py    ← 业务逻辑：StudentManager 类 + 生成器
├── utils.py       ← 工具：@log_call 装饰器 + 日志
└── main.py        ← CLI 入口
```

### 知识覆盖

| 知识点 | 文件 | 用法 |
|--------|------|------|
| 类继承 | models.py | `Person → Student → Monitor` 三级 |
| super().__init__() | models.py | 子类调父类构造 |
| 方法重写 | models.py | `Monitor.__str__()` 覆盖 `Student.__str__()` |
| 多态 + isinstance | services.py | 遍历 Person 列表时判断类型 |
| @property | models.py | `Student.score` setter 校验 0-100 |
| 私有属性 | models.py | `Student.__scores` 历史成绩列表 |
| 自定义装饰器 | utils.py | `@log_call` 记录方法调用到日志 |
| 生成器 yield | services.py | `filter_students()` 逐个 yield |
| 模块/import | 全部 | 4 个文件互引用 |
| `__name__ == "__main__"` | main.py | 程序入口 |

---

## 二、英语任务

### 单词（15min）

30 个六级高频词 #181-210（见 `Day07_单词自测.txt`）

### 听力（15min）

VOA 常速精听 1 篇，听不懂的倒回去反复听。

---

## 三、Git

```bash
git add .
git commit -m "Day7: 学生管理系统（Week 2 收官，多文件项目）"
git push
```

---

## 检查清单

- [ ] models.py 写完了，三级继承能跑
- [ ] @property 成绩校验生效（输入 150 会报错）
- [ ] @log_call 装饰器能记录每次方法调用
- [ ] filter_students() 生成器能逐个筛选
- [ ] main.py 的循环菜单交互正常
- [ ] 单词自测填完
- [ ] VOA 听力完成
- [ ] commit + push
