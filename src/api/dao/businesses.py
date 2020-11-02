from api.util.config import db
from api.dao.users import Users

class Businesses(db.Model):
    __tablename__ = 'businesses'
    business_id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(5), nullable=False)
    business_email = db.Column(db.String(150), nullable=False)
    business_phone = db.Column(db.String(12), nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)
    business_owner_id = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.serviceId'), nullable=True)
    
    appointment = db.relationship("Appointment")

    def __init__(self, **args):
        self.business_name = args.get('business_name')
        self.business_email = args.get('business_email')
        self.business_phone = args.get('business_phone')
        self.address = args.get('address')
        self.city = args.get('city')
        self.zip_code = args.get('zip_code')
        self.max_capacity = args.get('max_capacity')
        self.business_owner_id = args.get('business_ownerId')
        self.service_id = args.get('serviceId')

    @property
    def primaryKey(self):
        return self.business_id

    @staticmethod
    def getBusinesses():
        return Businesses().query.all()
    
    @staticmethod
    def getBusinessById(bid):
        return Businesses().query.filter_by(business_id=bid).first()

    @staticmethod
    def getAllBusinessByCity(ct):
        return Businesses().query.filter_by(city=ct).all()

    @staticmethod
    def getAllBusinessByZipCode(zp):
        return Businesses().query.filter_by(zip_code=zp).all()
    
    @staticmethod
    def getAllBusinessByMaxCapacity(mc):
        return Businesses().query.filter_by(max_capacity=mc).all()

    @staticmethod
    def getBusinessByService(sid):
        return Businesses().query.filter_by(service_id=sid).all()

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @staticmethod
    def updateRole(uid):
        user = Users.getUserById(uid)
        user.role = 'owner'
        db.session.commit()
        return user