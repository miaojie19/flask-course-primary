from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired
from userauth_demo.models import User


class LoginForm(FlaskForm):
    # 表单包括邮箱，密码和是否记住密码及一个提交按钮
    email = EmailField('Email', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class registerForm(FlaskForm):
    username = StringField('Username',
                             validators=[DataRequired(), Length(min=2,max=20)])
    email = EmailField("Email",
                         validators=[DataRequired(), Length(min=2,max=20)])
    password = PasswordField('Password',
                              validators=[InputRequired(), EqualTo("confirm_password", message="Passwords must match")])
    confirm_password = PasswordField('Confirm Password',
                                      validators=[DataRequired()])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


