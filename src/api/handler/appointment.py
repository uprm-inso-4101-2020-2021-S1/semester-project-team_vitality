from flask import jsonify, session
from api.dao.appointment import Appointment
from api.dao.businesses import Businesses
from api.util.utilities import Utilities
from api.dao.users import Users
import datetime as dt
import pytz

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
                "appointments": appt_list                
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
    
    @staticmethod
    def getApptById(aid):
        try:
            appt = Appointment.getApptById(aid)
            appt_dict = Utilities.to_dict(appt)
            result = {
                "message": "Success!",
                "appointment": appt_dict                
            }
            return jsonify(result), 200
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
                "appointments": appt_list,        
            }
            return jsonify(result), 200
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
                "appointments": appt_list                
            }
            return jsonify(result), 200
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
                "appointments": appt_list                
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def createAppt(json):
        validParams = Utilities.verify_parameters(json, ['business_id', 'business_name', 'start_time', 'end_time'])
        validParams['business_name'] = Businesses().getBusinessById(validParams['business_id']).business_name
        if validParams:
            try:
                newAppt = Appointment(**validParams).create()
                newAppt.business_name = Businesses().getBusinessById(validParams['business_id']).business_name
                result = {
                    "message": "Success!",
                    "request": Utilities.to_dict(newAppt)
                }
                return jsonify(result), 200
            except Exception as e:
                return jsonify(reason="Server error", error=e.__str__()), 500
        else:
            return jsonify(reason="Invalid parameters"), 400
    
    @staticmethod
    def userRegisterAppt(aid, uid):
        validParams = Utilities.verify_parameters(json, ['number_of_customers'])
        try:
            appt = Appointment.updateAppt(aid, uid)
            result = {
                "message": "Success!",
                "request": Utilities.to_dict(appt)
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def userCancelAppt(aid):
        try:
            checkAppt = Appointment.getApptById(aid)
            if(checkAppt.user_id == None):
                return jsonify(reason="Appointment does not have a customer register"), 406
            appt = Appointment.cancelAppt(aid)
            result = {
                "message": "Success!",
                "request": Utilities.to_dict(appt)
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

