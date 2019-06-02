from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URE'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

