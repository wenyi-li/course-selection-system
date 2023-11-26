from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    teacher = db.Column(db.String(50), nullable=False)

class SelectedCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    teacher = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    all_courses = Course.query.all()
    available_courses = [course for course in all_courses if course not in SelectedCourse.query.all()]
    selected_courses = SelectedCourse.query.all()

    return render_template('index.html', available_courses=available_courses, selected_courses=selected_courses)

@app.route('/select_course/<int:course_id>', methods=['POST'])
def select_course(course_id):
    course = Course.query.get(course_id)
    if course and course not in SelectedCourse.query.all():
        # 将课程添加到已选课程
        selected_course = SelectedCourse(name=course.name, number=course.number, teacher=course.teacher)
        db.session.add(selected_course)
        db.session.commit()

        # 删除可选课程列表中的课程
        db.session.delete(course)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/remove_course/<int:course_id>', methods=['POST'])
def remove_course(course_id):
    selected_course = SelectedCourse.query.get(course_id)
    if selected_course:
        # 从已选课程中删除
        db.session.delete(selected_course)
        db.session.commit()

        # 将删除的课程添加回可选课程列表
        course = Course(name=selected_course.name, number=selected_course.number, teacher=selected_course.teacher)
        db.session.add(course)
        db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        # 清空数据库
        db.drop_all()
        db.create_all()

        # 创建指定的三门课程
        course1 = Course(name='高级软件工程', number='CS101', teacher='Prof. 罗')
        course2 = Course(name='计算机算法设计', number='CS102', teacher='Prof. 陈')
        course3 = Course(name='高级操作系统', number='CS103', teacher='Prof. 李')
        course4 = Course(name='图像处理', number='CS104', teacher='Prof. 王')

        # 添加到数据库
        db.session.add(course1)
        db.session.add(course2)
        db.session.add(course3)
        db.session.add(course4)

        # 提交更改
        db.session.commit()

    app.run(debug=True)


