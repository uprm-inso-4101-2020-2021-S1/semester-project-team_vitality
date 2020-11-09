from flask import jsonify, session
from api.dao.businesses import Businesses
from api.util.utilities import Utilities
from api.dao.users import Users
import re

class BusinessesHandler:

    @staticmethod
    def getAllBusinesses():
        try:
            businesses = Businesses.getBusinesses()
            businesses_list = []
            for business in businesses:
                 businesses_list.append(Utilities.to_dict(business))
            result = {
                "message": "Success!",
                "businesses": businesses_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
    
    @staticmethod
    def getBusinessById(bid):
        try:
            business = Businesses.getBusinessById(bid)
            business_dict = Utilities.to_dict(business)
            result = {
                "message": "Success!",
                "business": business_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500


    @staticmethod
    def getAllBusinessesByCity(ct):
        try:
            businesses = Businesses.getAllBusinessesByCity(ct)
            businesses_list = []
            for business in businesses:
                 businesses_list.append(Utilities.to_dict(business))
            result = {
                "message": "Success!",
                "businesses": businesses_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getAllBusinessesByZipCode(zc):
        try:
            businesses = Businesses.getAllBusinessesByZipCode(zc)
            businesses_list = []
            for business in businesses:
                 businesses_list.append(Utilities.to_dict(business))
            result = {
                "message": "Success!",
                "businesses": businesses_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getAllBusinessesByMaxCapacity(mc):
        try:
            businesses = Businesses.getAllBusinessesByMaxCapacity(mc)
            businesses_list = []
            for business in businesses:
                 businesses_list.append(Utilities.to_dict(business))
            result = {
                "message": "Success!",
                "businesses": businesses_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getBusinessesByService(sid):
        try:
            businesses = Businesses.getBusinessesByService(sid)
            businesses_list = []
            for business in businesses:
                 businesses_list.append(Utilities.to_dict(business))
            result = {
                "message": "Success!",
                "businesses": businesses_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getBusinessByOwner(uid):
        try:
            business = Businesses.getBusinessByOwner(uid)
            business_dict = Utilities.to_dict(business)
            result = {
                "message": "Success!",
                "business": business_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def businessRegister(json):
        validParams = Utilities.verify_parameters(json, ['business_name', 'address', 'city', 'zip_code', 
        'business_email', 'business_phone', 'max_capacity', 'owner_id', 'service_id'])
        if validParams:
            try:
                if not re.match(r'[A-Za-z0-9]+', validParams['business_name']):
                    return jsonify(reason="Business name must contain only characters and numbers")
                if not re.match(r'[^@]+@[^@]+\.[^@]+', validParams['business_email']):
                    return jsonify(reason="Invalid email address")
                elif not re.search(r'\w{3}-\w{3}-\w{4}', validParams['business_phone']):
                    return jsonify(reason="The format for business phone is: ###-###-####")
                elif not re.match(r'[0-9]{5}', validParams['zip_code']):
                    return jsonify(reason="The format for zip code is: #####")
                elif not re.match(r'[0-9]', validParams['max_capacity']):
                    return jsonify(reason="Max capacity must be a number")
                Users.updateRole(validParams['owner_id'])
                newBusiness = Businesses(**validParams).create()
                result = {
                    "message": "Success!",
                    "request": Utilities.to_dict(newBusiness)
                }
                return jsonify(result), 200
            except Exception as e:
                return jsonify(reason="Server error", error=e.__str__()), 500
        else:
            return jsonify(reason="Invalid parameters"), 400
