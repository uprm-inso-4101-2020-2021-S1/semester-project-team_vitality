from .middlewares import login_required
from flask import Flask, json, g, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Endpoints represent the data you are sending/receiving
# Here is an example 
# You would need to import any and all objects you are using\
# for responses.

# @app.route("/kudos", methods=["GET"])
# @login_required
# def index():
#  return json_response(Kudo(g.user).find_all_kudos())