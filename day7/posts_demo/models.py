from posts_demo import db
from flask_login import UserMixin
from posts_demo import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    #print(user_id)
    return User.query.get(int(user_id))


# User继承UserMixin类
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60),  nullable=False)
    profile_image = db.Column(db.String(20), nullable=True)
    # 添加反向引用关系
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.password}')"


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, unique=True, nullable=False)
    publish_datetime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow())
    update_datetime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow())
    # 添加表user的外键user_id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.content}','{self.publish_datetime}')"
