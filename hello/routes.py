from hello import app


@app.route("/")
def index():
    return "hello,world"

