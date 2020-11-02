from flask import jsonify, session
from api.dao.users import Users
from api.util.utilities import Utilities

class UsersHandler:

    @staticmethod
    def getAllUsers():
        try:
            users = Users.getUsers()
            users_list = []
            for user in users:
                users_list.append(Utilities.to_dict(user))
            result = {
                "message": "Success!",
                "users": users_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500


    @staticmethod
    def getUserById(uid):
        try:
            user = Users.getUserById(uid)
            user_dict = Utilities.to_dict(user)
            result = {
                "message": "Success!",
                "users": user_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
    
    @staticmethod
    def getUserByEmail(uemail):
        try:
            user = Users.getUserByEmail(uemail)
            user_dict = Utilities.to_dict(user)
            result = {
                "message": "Success!",
                "users": user_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
    
    @staticmethod
    def getOwners():
        try:
            owners = Users.getOwners()
            owners_list = []
            for owner in owners:
                owners_list.append(Utilities.to_dict(owner))
            result = {
                "message": "Success!",
                "users": owners_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
    
    @staticmethod
    def getCustomers():
        try:
            customers = Users.getCustomers()
            customers_list = []
            for customer in customers:
                customers_list.append(Utilities.to_dict(customer))
            result = {
                "message": "Success!",
                "users": customers_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def login(json):
        try:
            if json['username'] == "" or json['password'] == "":
                return jsonify(reason="Must fill username and password fields"), 400
            user = Users.getUserByUsername(json['username'])
            user_dict = Utilities.to_dict(user)
            if user and user.password == json['password']:
                session['logged_in'] = True
                result = {
                    "message": "Success!",
                    "user": user_dict
                }
                return jsonify(result), 200
            else:
                return jsonify(reason="Incorrect username or password"), 401
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
    
    @staticmethod
    def logout():
        try:
            session['logged_in'] = False
            return jsonify(status='Success!'), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500