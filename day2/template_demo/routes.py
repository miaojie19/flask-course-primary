from flask import render_template     # 从flask库中导入render_template对象
from template_demo import app         # 从template_demo包中导入app实例


@app.route('/')
def index():
    user = {'username':'猫姐'}         # 建立一个user字典
    return render_template('index.html', title='HomePage', html_user=user)


