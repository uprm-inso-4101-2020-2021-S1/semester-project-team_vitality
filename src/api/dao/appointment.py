from api.util.config import db
from api.dao.users import Users
from api.dao.businesses import Businesses
from random import randint
import datetime

class Appointment(db.Model):
    __tablename__ = 'appointment'
    apptid = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc).astimezone)
    end_time = db.Column(db.DateTime)
    confirmation_number = db.Column(db.Integer, nullable=True)
    businessid = db.Column(db.Integer, db.ForeignKey('businesses.businessid'), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), nullable=True)

    def __init__(self, **args):
        self.start_time = args.get('start_time')
        self.end_time = args.get('end_time')
        self.confirmation_number = args.get('confirmation_number')
        self.businessId = args.get('businessid')
        self.userid = args.get('userid')
    
    @property
    def primaryKey(self):
        return self.apptid

    @staticmethod
    def getApptById(aid):
        return Appointment().query.filter_by(apptid=aid).first()

    @staticmethod
    def getApptByUser(uid):
        return Appointment().query.filter_by(userid=uid).all()
    
    @staticmethod
    def getApptByBusiness(bid):
        return Appointment().query.filter_by(businessid=bid).all()

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @staticmethod
    def updateAppt(aid, uid):
        appt = Appointment.getApptById(aid)
        appt.userid = uid
        appt.confirmation_number = randint(0,1000)
        db.session.commit()
        return appt

    @staticmethod
    def cancelAppt(aid):
        appt = Appointment.getApptById(aid)
        appt.userid = None
        appt.confirmation_number = None
        db.session.commit()
        return appt
    



