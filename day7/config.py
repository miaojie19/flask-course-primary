import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    # 使用表单,对Flask_WTF进行配置
    SECRET_KEY = 'miaojie is great!'
    PROFILE_PATH = "profile/"


