from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.secret_key = "vitality"

db = SQLAlchemy(app)
CORS(app)