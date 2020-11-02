from api.util.config import db

class Services(db.Model):
    __tablename__ = 'services'
    serviceId = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(50), nullable=False)

    business = db.relationship("Businesses")

    def __init__(self, **args):
        self.service_name = args.get('service_name')

    def __repr__(self):
        return self.service_name
    
    @property
    def primaryKey(self):
        return self.service_id

    @staticmethod
    def getServices():
        return Services().query.all()
    
    @staticmethod
    def getServiceById(sid):
        return Services().query.filter_by(serviceId=sid).first()