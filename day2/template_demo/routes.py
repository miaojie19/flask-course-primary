from flask import render_template     # 从flask库中导入render_template对象
from template_demo import app         # 从template_demo包中导入app实例


@app.route('/')
def index():
    user = {'username': '猫姐'}
    # 日志由一个列表组成，其中里面包含两个字典，里面各有author和content字段
    posts = [
        {
            'author': {'username': '猫姐'},
            'content': 'This day is Beautiful day!'
        },
        {
            'author': {'username': '猫哥'},
            'content': 'The flower is beautiful!'
        }
    ]
    return render_template('index.html', title='Home', html_user=user, html_posts=posts)


