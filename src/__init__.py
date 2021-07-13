from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config["DEBUG"] = False
app.config["SECRET_KEY"] = '12345'
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://Raquel:12345678@127.0.0.1:3306/engs"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SQLALCHEMY_ECHO "] = True
