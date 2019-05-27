# 从form_demo包中导入app实例
from flask import render_template, flash
from form_demo import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
     username = StringField('Username', validators=[DataRequired()])
     password = PasswordField('Password', validators=[DataRequired()])
     remember = BooleanField('Remember Me')
     submit = SubmitField('Sign In')


@app.route('/login', methods=['GET', 'POST'])
def login():
     form = LoginForm()
     # 添加能够处理post请求
     if form.validate_on_submit():
          flash('登录用户 {},记住remember状态{}成功'.format(form.username.data, form.remember.data), 'success')
     return render_template('form.html', title='第三天', html_form=form)
