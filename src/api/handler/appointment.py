from flask import jsonify, session
from api.dao.appointment import Appointment
from api.dao.businesses import Businesses
from api.util.utilities import Utilities
from api.dao.users import Users

class AppointmentHandler:

    @staticmethod
    def getAllAppointments():
        try:
            appointments = Appointment.getAppointments()
            appt_list = []
            for appt in appointments:
                appt_list.append(Utilities.to_dict(appt))
            result = {
                "message": "Success!",
                "businesses": appt_list                
            }
            return jsoinfy(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
    
    @staticmethod
    def getApptById(aid):
        try:
            appt = Appointment.getApptById(aid)
            appt_dict = Utilities.to_dict(appt)
            result = {
                "message": "Success!",
                "businesses": appt_dict                
            }
            return jsoinfy(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
    
    @staticmethod
    def getAllUserAppt(uid):
        try:
            appointments = Appointment.getApptByUser(uid)
            appt_list = []
            for appt in appointments:
                appt_list.append(Utilities.to_dict(appt))
            result = {
                "message": "Success!",
                "businesses": appt_list                
            }
            return jsoinfy(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getAllBusinessAppt(bid):
        try:
            appointments = Appointment.getApptByBusiness(bid)
            appt_list = []
            for appt in appointments:
                appt_list.append(Utilities.to_dict(appt))
            result = {
                "message": "Success!",
                "businesses": appt_list                
            }
            return jsoinfy(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getApptByStartTime(dt):
        try:
            appointments = Appointment.getApptByStartTime(dt)
            appt_list = []
            for appt in appointments:
                appt_list.append(Utilities.to_dict(appt))
            result = {
                "message": "Success!",
                "businesses": appt_list                
            }
            return jsoinfy(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

