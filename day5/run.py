from userauth_demo import app  # 从userauth_demo包中导入app实例

if __name__ == "__main__":
    app.run(debug=True, port=5005)        # app实例调用自己的run函数

