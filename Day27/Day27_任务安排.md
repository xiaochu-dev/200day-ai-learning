# Day 27 — GitHub 实战：Issues / Pull Request / Code Review / Actions

> Week 4 Git 版本控制周 | 2026-08-12（周三）

---

## 今日目标

不写脚本，**真正上 GitHub 操作**。学会使用 Issues（任务跟踪）、Pull Request（代码审查）、Code Review（审查流程）、Actions（CI/CD 自动化）。

---

## 一、GitHub Issues — 任务跟踪

Issue 是 GitHub 的轻量级"任务卡片"，用于跟踪 bug、功能需求、改进建议等。

### Issue 的核心要素

| 元素 | 用途 |
|------|------|
| **标题** | 一句话描述要做什么 |
| **描述** | 详细说明（可用 Markdown） |
| **Labels** | 分类标签（bug / feature / enhancement / documentation） |
| **Assignee** | 谁负责处理 |
| **Milestone** | 归到哪个里程碑/版本 |

### Issue 最佳实践

**好的 Issue**：
```markdown
## 问题描述
点击"登录"按钮后页面无响应，控制台报错 `Uncaught TypeError: Cannot read properties of null`

## 复现步骤
1. 打开登录页面
2. 输入用户名密码
3. 点击登录按钮
4. 页面卡住，无任何响应

## 期望行为
点击登录后应发送请求，成功跳转首页，失败显示错误提示

## 环境
- 浏览器：Chrome 120
- OS：Windows 10
```

**差的 Issue**：「登录按钮坏了」（信息太少，无法复现）

---

## 二、Pull Request — 请求合并代码

PR 是 GitHub 的**核心协作机制**。你做了一个功能/修复，通过 PR 请求合并到目标分支。

### PR 的生命周期

```
1. 创建分支 → 2. 开发提交 → 3. 推送分支 → 4. 创建 PR
    ↓
5. Code Review → 6. 修改 + 推送更新 → 7. 通过审查 → 8. Merge PR
```

### 创建 PR 的完整流程

```bash
# 1. 从 main 切出功能分支
git switch -c feature/add-readme

# 2. 做改动并提交
echo "# My Project" > README.md
git add README.md
git commit -m "docs: add README"

# 3. 推送到 GitHub
git push -u origin feature/add-readme

# 4. 去 GitHub 网页上点击 "Compare & pull request"
#    - 写 PR 标题和描述
#    - 选择 base 分支（目标，通常是 main）
#    - 选择 compare 分支（源，你的 feature 分支）
#    - 点击 "Create pull request"
```

### PR 描述模板

```markdown
## 做了什么
简要描述这个 PR 的改动

## 为什么这么做
说明原因和背景

## 测试计划
- [ ] 手动测试：登录 → 首页 → 退出
- [ ] 单元测试：`npm test` 全部通过

## Screenshots（如适用）
粘贴截图

## 关联 Issue
Closes #123
```

---

## 三、Code Review — 代码审查

### 审查者看什么

| 维度 | 检查点 |
|------|--------|
| **正确性** | 逻辑对不对？边界条件处理了吗？ |
| **安全性** | 有没有注入漏洞？密钥泄露了吗？ |
| **可读性** | 命名清晰吗？结构合理吗？ |
| **性能** | 有 N+1 查询吗？有不必要的循环吗？ |
| **测试** | 相关测试写了吗？覆盖率够吗？ |

### 如何看 diff

在 PR 页面，GitHub 会展示所有改动的 diff：

```
- 红色行：删除的内容
+ 绿色行：新增的内容
```

### Review 动作

| 动作 | 含义 |
|------|------|
| **Comment** | 提个问题/建议，不表态 |
| **Approve** | 审查通过，可以合并 |
| **Request changes** | 有问题需要改，改了再看 |

---

## 四、GitHub Actions — CI/CD 自动化

### 概念

Actions 让你在代码 push/PR/发布 时**自动执行任务**：

- 每次 push 自动跑测试
- PR 创建时自动做代码检查
- 合并到 main 后自动部署

### 工作方式

在项目根目录创建 `.github/workflows/<name>.yml`：

```yaml
# .github/workflows/test.yml
name: Run Tests

on:
  push:            # 每次 push 时触发
    branches: [main]
  pull_request:    # 每次 PR 时触发
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4    # 拉取代码
      - uses: actions/setup-python@v5 # 装 Python
        with:
          python-version: '3.12'
      - run: pip install pytest     # 装依赖
      - run: pytest                 # 跑测试
```

### 在哪里看

GitHub 仓库顶部 → **Actions** 标签 → 查看所有工作流运行记录。

---

## 五、今日任务清单（全在浏览器中操作）

> 以下操作需要你有一个 GitHub 账号，在 `200day` 仓库（或任意测试仓库）上完成。

### Part 1：Issues

- [ ] 创建一个 Issue，标题："[学习] Git 分支操作笔记总结"
  - 在描述中用 Markdown 写上你今天学会的 3 个 Git 分支命令
  - 添加 label：`documentation`
  - 然后自己 Close 掉这个 Issue

### Part 2：Pull Request
- [ ] 创建一个新分支 `feature/day27-github-notes`（本地或远程都行）
- [ ] 在分支上创建一个 `Day27/GitHub学习笔记.md` 文件，写 200-300 字的学习笔记
- [ ] 提交并推送到 GitHub
- [ ] 在 GitHub 网页上创建一个 Pull Request，base 设为 `main`
- [ ] 在 PR 描述中写明：改了什么、为什么、测试方式
- [ ] 自己 Review 这个 PR（文件改动页面），确认 diff 正确
- [ ] Merge PR → 选择 "Squash and merge"（把所有提交压缩成一个）
- [ ] 删除远程分支（GitHub 页面会提示）

### Part 3：了解 Squash / Merge / Rebase 的区别
Merge PR 时有三种方式：

| 方式 | 效果 | 历史 |
|------|------|------|
| **Merge commit** | 生成一个 merge commit | 保留所有分支历史 |
| **Squash and merge** | 所有提交压缩成一个 | 简洁，但丢失细粒度历史 |
| **Rebase and merge** | 把提交 rebase 到 base 分支 | 直线历史，无 merge commit |

- [ ] 了解三种方式，写一句自己的理解记录在笔记中

### Part 4：Actions

- [ ] 打开你的 GitHub 仓库 → Actions 标签
- [ ] 了解 Actions 页面展示什么信息
- [ ] 如果有已有的 workflow 运行记录，点进去看日志
- [ ] （可选）创建一个简单的 Action：参考上面的例子，新建 `.github/workflows/hello.yml`：
  ```yaml
  name: Hello World
  on: [push]
  jobs:
    say-hello:
      runs-on: ubuntu-latest
      steps:
        - run: echo "Hello from GitHub Actions!"
  ```

### 英语
- [ ] VOA 精听 15 分钟

### 收尾
- [ ] Issue 已创建并关闭
- [ ] PR 已创建、审查、合并
- [ ] 理解了三种 merge 方式的区别
- [ ] 提交：
  ```
  cd E:\Users\MyFiles\Desktop\200day
  git add Day27/
  git commit -m "Day27: GitHub实战——Issues/Pull Request/Code Review/Actions"
  git push
  ```

---

## 六、提示

1. **用哪个仓库练习？**——可以直接用 `200day` 仓库（建议先备份），或者创建 `test-github-practice` 测试仓库
2. **不要怕 PR 写得不好**——哪怕只有一行改动，走一遍完整流程才能理解
3. **Review 自己的代码是重要习惯**——提交前自己先看一遍 diff，很多问题自己能发现
4. **Actions 可以先跳过**——如果觉得 CI/CD 离现在的阶段太远，先了解概念，后续实战时再深入
