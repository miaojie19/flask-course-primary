from posts_demo import app  # 从posts_demo包中导入app实例
from config import Config
app.config.from_object(Config)
if __name__ == "__main__":
    app.run(debug=True, port=5005)        # app实例调用自己的run函数

