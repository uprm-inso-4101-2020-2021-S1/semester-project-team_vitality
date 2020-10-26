#Arrange All Models
class User:
    def __init__(self, userId=None, username=None, password=None, email=None, 
    first_name=None, last_name=None, role=None):
        self.userId = userId
        self.username = username
        self.password = password
        self.email = email
        self.first_name =  first_name
        self.last_name = last_name
        self.role = role

class Business:
    def __init__(self, businessId=None, business_name=None, business_email=None, 
    business_phone=None, address=None, city=None, zip_code=None, max_capacity=None,
    business_ownerId=None):
        self.businessId = businessId
        self.business_name = business_name
        self.business_email = business_email
        self.business_phone = business_phone
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.max_capacity = max_capacity
        self.business_ownerId = business_ownerId

class Service:
    def __init__(self, serviceId=None, service_name=None, business=None):
        self.serviceId = serviceId
        self.service_name = service_name
        self.business = business

class Appointment:
    def __init__(self, appointmentId=None, customer=None, service=None, start_time=None, end_time=None, confirmation_number=None):
        self.appointmentId = appointmentId
        self.customer = customer
        self.service = service
        self.start_time = start_time
        self.end_time = end_time
        self.confirmation_number = confirmation_number
