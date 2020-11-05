from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db_user = ''
db_password = ''
db_host = ''
db_name = ''

db_uri = f'postgres://{db_user}:{db_password}@{db_host}/{db_name}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.secret_key = "vitality"

db = SQLAlchemy(app)
CORS(app)