from flask import jsonify, session
from api.dao.businesses import Businesses
from api.util.utilities import Utilities

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
                "businesses": business_dict
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
                "businesses": business_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500