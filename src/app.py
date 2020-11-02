from flask import request
from api.util.config import app
from api.handler.services import ServicesHandler
from api.handler.users import UsersHandler
from api.handler.businesses import BusinessesHandler

@app.route('/', methods=['GET'])
def home():
    return "Hi"

@app.route('/users', methods=['GET'])
def getAllUsers():
    return UsersHandler.getAllUsers()

@app.route('/users/<int:uid>', methods=['GET'])
def getUserById(uid):
    return UsersHandler.getUserById(uid)

@app.route('/owners', methods=['GET'])
def getOwners():
    return UsersHandler.getOwners()

@app.route('/customers', methods=['GET'])
def getCustomers():
    return UsersHandler.getCustomers()

@app.route('/services', methods=['GET'])
def getAllServices():
    return ServicesHandler.getAllServices()

@app.route('/services/<int:sid>', methods=['GET'])
def getServicesById(sid):
    return ServicesHandler.getServiceById(sid)

@app.route('/businesses', methods=['GET'])
def getAllBusinesses():
    return BusinessesHandler.getAllBusinesses()

@app.route('/businesses/<int:bid>', methods=['GET'])
def getBusinessById(bid):
    return BusinessesHandler.getBusinessById(bid)

@app.route('/businesses/services/<int:sid>', methods=['GET'])
def getBusinessesByService(sid):
    return BusinessesHandler.getBusinessesByService(sid)

@app.route('/businesses/owner/<int:uid>', methods=['GET'])
def getBusinessByOwner(uid):
    return BusinessesHandler.getBusinessByOwner(uid)

@app.route('/businesses/city/<ct>', methods=['GET'])
def getAllBusinessesByCity(ct):
    return BusinessesHandler.getAllBusinessesByCity(ct)

@app.route('/businesses/zipcode/<zc>', methods=['GET'])
def getAllBusinessesByZipCode(zc):
    return BusinessesHandler.getAllBusinessesByZipCode(zc)

@app.route('/businesses/maxcapacity/<mc>', methods=['GET'])
def getAllBusinessesByMaxCapacity(mc):
    return BusinessesHandler.getAllBusinessesByMaxCapacity(mc)

@app.route('/user/register', methods=['POST'])
def userRegister():
    return UsersHandler.register(request.json)

@app.route('/business/register', methods=['POST'])
def businessRegister():
    return BusinessesHandler.businessRegister(request.json)

@app.route('/login', methods=['POST'])
def login():
    return UsersHandler.login(request.json)

@app.route('/logout', methods=['GET'])
def logout():
    return UsersHandler.logout()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')