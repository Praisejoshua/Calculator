from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Set a secret key
app.config['SECRET_KEY'] = 'BBC_forever'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculations.db'

db = SQLAlchemy(app)

from package import routes