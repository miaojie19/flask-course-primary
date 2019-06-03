#!coding:utf8
from database_demo import db, app


class User(db.Model):
    __table__name = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=True)
    #添加反向引用关系
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class Post(db.Model):
    __table__name = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=True)
    # 添加user_id外键，它建立表user和表post的联系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}')"


@app.shell_context_processor
def generate_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

