from api.util.config import db
from api.dao.users import Users
from api.dao.businesses import Businesses
from random import randint
import datetime

class Appointment(db.Model):
    __tablename__ = 'appointment'
    appt_id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    confirmation_number = db.Column(db.Integer, nullable=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.businessId'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=True)

    def __init__(self, **args):
        self.start_time = args.get('start_time')
        self.end_time = args.get('end_time')
        self.confirmation_number = args.get('confirmation_number')
        self.business_id = args.get('businessId')
        self.user_id = args.get('userId')
    
    @property
    def primaryKey(self):
        return self.appt_id

    @staticmethod
    def getApptById(aid):
        return Appointment().query.filter_by(appt_id=aid).first()

    @staticmethod
    def getApptByUser(uid):
        return Appointment().query.filter_by(user_id=uid).all()
    
    @staticmethod
    def getApptByBusiness(bid):
        return Appointment().query.filter_by(business_id=bid).all()

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @staticmethod
    def updateAppt(aid, uid):
        appt = Appointment.getApptById(aid)
        appt.user_id = uid
        appt.confirmation_number = randint(0,1000)
        db.session.commit()
        return appt

    @staticmethod
    def cancelAppt(aid):
        appt = Appointment.getApptById(aid)
        appt.user_id = None
        appt.confirmation_number = None
        db.session.commit()
        return appt
    



