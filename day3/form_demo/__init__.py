from flask import Flask    # 从flask包中导入Flask类

app = Flask(__name__)      # 通过Flask类创建一个app实例

app.config['SECRET_KEY'] = 'miaojie is great!'  # 对Flask进行配置

from form_demo import routes

