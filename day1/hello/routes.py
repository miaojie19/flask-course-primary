from hello import app


@app.route("/")
def index():
    return "你好，喵星在线！"

