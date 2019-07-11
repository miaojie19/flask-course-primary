#!coding:utf8
from flask import render_template, redirect, url_for, flash, request
from posts_demo import app
# 从posts_demo.forms中导入LoginForm类
from posts_demo.forms import LoginForm, UpdateAccountForm
from flask_login import current_user, login_user, login_required, logout_user
from posts_demo.models import User
from posts_demo.forms import registerForm
from posts_demo import db, bcrypt
from flask import current_app
from posts_demo.utils import save_user_face_image
from posts_demo.forms import CreatePostForm
from posts_demo.models import Post
from datetime import datetime


# 添加视图函数渲染主页内容
@app.route('/')
@login_required
def index():
    post = Post.query.all()
    return render_template('index.html', title='第七天', html_post=post)


@app.route("/account", methods=["GET", "POST"])
def account():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = UpdateAccountForm()
    profile_image = current_user.profile_image
    if profile_image:
        profile_image = current_app.config["PROFILE_PATH"] + profile_image
    else:
        profile_image = current_app.config["PROFILE_PATH"] + "default.jpg"

    if request.method == "POST":
        username = form.username.data
        email = form.email.data
        if form.profile_image.data:
            picture_file = save_user_face_image(form.profile_image.data)
            current_user.profile_image = picture_file
        current_user.username = username
        current_user.email = email
        db.session.commit()
        return redirect(url_for("account"))
    form.email.data = current_user.email
    form.username.data = current_user.username
    return render_template("account.html", title="第七天", html_user=current_user, html_form=form, html_user_image=profile_image)


# 添加视图函数渲染表单登陆内容
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # 对类LoginForm的实例
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            nextpage = request.args.get('next')
            if nextpage:
                return redirect(nextpage)
            else:
                url = url_for('index')
                return redirect(url)
        else:
            flash('登陆不成功，请检查邮箱和密码！', 'danger')
    return render_template('login.html', title='第七天', html_form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = registerForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password,\
                    profile_image="default.jpg")
        db.session.add(user)
        db.session.commit()
        flash('注册成功，请登陆！', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="第七天", html_form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/create/post", methods=["GET", "POST"])
@login_required
def create_post():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = CreatePostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        # utc_now = datetime.utcnow()
        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('你的日志创建成功', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', title="第七天", html_form=form)


@app.route("/post/<int:post_id>")
@login_required
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("show_post.html", title=post.title, html_post=post)


@app.route("/user/post/<string:username>")
def show_user_post(username):
    #查该用户发表的所有日志
    user = User.query.filter_by(username=username).first()
    posts = user.posts
    title = username +"的日志"
    return render_template('index.html', title=title, html_post=posts)

# @app.route("/post/delete/<int:post_id>", methods=["POST"])
# @login_required
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     db.session.delete(post)
#     db.session.commit()
#     return redirect(url_for("index"))






