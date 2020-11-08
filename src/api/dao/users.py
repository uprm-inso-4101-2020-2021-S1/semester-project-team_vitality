from api.util.config import db

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    role = db.Column(db.String(10), nullable=False)

    business = db.relationship("Businesses")
    appointment = db.relationship("Appointment")

    def __init__(self, **args):
        self.first_name = args.get('first_name')
        self.last_name = args.get('last_name')
        self.email = args.get('email')
        self.password = args.get('password')
        self.username = args.get('username')
        self.role = args.get('role')

    @property
    def primaryKey(self):
        return self.user_id
    
    @staticmethod
    def getUsers():
        return Users().query.all()

    @staticmethod
    def getUserById(uid):
        return Users().query.filter_by(user_id=uid).first()
    
    @staticmethod
    def getUserByEmail(uemail):
        return Users().query.filter_by(email=uemail).first()
    
    @staticmethod
    def getUserByUsername(uname):
        return Users().query.filter_by(username=uname).first()
    
    @staticmethod
    def getOwners():
        return Users().query.filter_by(role='owner').all()
    
    @staticmethod
    def getCustomers():
        return Users().query.filter_by(role='customer').all()
    
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
        
