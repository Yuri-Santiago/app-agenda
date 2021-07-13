from flask import Flask
from flask_session import Session

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "senha"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

from src.controllers import router
