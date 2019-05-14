from flask import Flask

app = Flask(__name__)

from hello import routes
