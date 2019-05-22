from template_demo import app


@app.route('/')
def index():
    user = {'username':'猫姐'}                        # 建立一个user字典
    return '''                                       # 返回HTML标记语言
    <html>
      <head>
        <title>Home Page-模板的使用-喵星在线</title>
      </head>
      <body>
        <h1>Hello,''' + user['username'] + '''!</h1>
      </body>
    </html>'''

