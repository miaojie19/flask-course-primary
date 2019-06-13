#!coding:utf8
from flask import render_template, redirect, url_for, flash
from userauth_demo import app
# 从userauth_demo.forms中导入LoginForm类
from userauth_demo.forms import LoginForm
from flask_login import current_user, login_user
from userauth_demo.models import User
from userauth_demo.forms import registerForm
from userauth_demo import db, bcrypt


# 添加视图函数渲染主页内容
@app.route('/')
def index():
    return render_template('index.html', title='第五天')


# 添加视图函数渲染表单登陆内容
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    # 对类LoginForm的实例
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == '424277539@qq.com' and form.password.data == 'miaojie':
            flash('Login Unsuccessful.', 'success')
            return redirect(url_for('index'))

    # 将视图函数中的变量form传到模板login.html文件中去
    return render_template('login.html', title='第五天', html_form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = registerForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="第五天", html_form=form)






