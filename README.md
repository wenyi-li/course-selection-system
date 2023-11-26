# 模拟选课系统

> 国科大2023高级软件工程课程作业

> 姓名：李文毅  学号：202318015059008

此项目是一个模拟选课系统，使用 Flask、Python、HTML 和 CSS 构建。它允许用户查看和选择课程，管理已选课程，并提交个人信息。

## 功能

- 查看可用课程列表。
- 在“可选课程”和“已选课程”部分选择和管理课程。
- 提交个人信息（姓名和学号）以进行选课。
- 在成功提交选课后收到成功消息。

## 使用指南

### 依赖库

- Flask
- Flask-SQLAlchemy

### 安装

1. 克隆仓库：

   ```
   git clone https://github.com/wenyi-li/course-selection-system.git
   cd course-selection-system
   ```

2. 创建虚拟环境：

   ```
   python -m venv venv
   ```

3. 激活虚拟环境：

   - 在 Windows 上：

     ```
     venv\Scripts\activate
     ```

   - 在 macOS 和 Linux 上：

     ```
     source venv/bin/activate
     ```

4. 安装依赖项：

   ```
   pip install -r requirements.txt
   ```

5. 运行应用程序：

   ```
   python app.py
   ```

6. 打开你的 Web 浏览器，访问 [http://localhost:5000](http://localhost:5000/)。

## 使用

1. 在你的 Web 浏览器中访问 [http://localhost:5000](http://localhost:5000/)。
2. 浏览可选课程列表。
3. 在“可选课程”和“已选课程”部分选择和管理课程。
4. 在“个人信息”部分提交你的个人信息。
5. 单击“提交选课”按钮完成选课。
6. 收到选课成功消息。

## 致谢

- 感谢 Flask 和 Python 社区提供的出色工具和文档。
