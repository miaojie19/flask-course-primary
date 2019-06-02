from database_demo import db


class User(db.Model):
    __table__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"


class Post(db.Model):
    __table__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}')"
