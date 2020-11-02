from flask import jsonify
from api.dao.services import Services
from api.util.utilities import Utilities

class ServicesHandler:

    @staticmethod
    def getAllServices():
        try:
            services = Services.getServices()
            service_list = []
            for svc in services:
                service_list.append(Utilities.to_dict(svc))
            result = {
                "message": "Success!",
                "services": service_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(message="Server error", error=e.__str__()), 500
    
    @staticmethod
    def getServiceById(sid):
        try:
            service = Services.getServiceById(sid)
            service_dict = Utilities.to_dict(service)
            result = {
                "message": "Success!",
                "services": service_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(message="Server error", error=e.__str__()), 500   