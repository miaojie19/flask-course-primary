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
     return render_template('form.html', title='第三天', html_form=form)
