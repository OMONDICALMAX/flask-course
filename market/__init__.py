from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY'] = '4e2ad04a96a00881dd9ded54'
db = SQLAlchemy(app)

from market import route