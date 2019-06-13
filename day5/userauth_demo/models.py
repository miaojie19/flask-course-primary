from userauth_demo import db
from flask_login import UserMixin
from userauth_demo import login_manager


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

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.password}')"


