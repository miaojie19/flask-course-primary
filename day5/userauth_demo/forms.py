from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField, BooleanField, SubmitField, StringField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired
from userauth_demo.models import User


class LoginForm(FlaskForm):
    # 表单包括邮箱，密码和是否记住密码及一个提交按钮
    email = EmailField(u'邮箱', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember = BooleanField(u'记住我')
    submit = SubmitField(u'登陆')


class registerForm(FlaskForm):
    username = StringField(u'用户名',
                             validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField(u"邮箱",
                         validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(u'密码',
                              validators=[InputRequired(), EqualTo(u"confirm_password", message="两次输入的密码不一致！")])
    confirm_password = PasswordField(u'确认密码',
                                      validators=[DataRequired()])
    submit = SubmitField(u'注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('该用户名已被注册！')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('该邮箱已被注册！')


