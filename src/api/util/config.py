from flask import Flask
from flask_cors import CORS
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db_host = 'sql9.freemysqlhosting.net'
db_user = 'sql9372928'
db_password = 'MJAV5SRze6'
db_name = 'sql9372928'

db_connection = f'mysql://{db_user}:{db_password}@{db_host}/{db_name}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
app.secret_key = "vitality"

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)
CORS(app)