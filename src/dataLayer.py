from flask_mysqldb import MySQL
import MySQLdb.cursors
from queryManager import QueryManager

class DataLayer(object):
    """
    The Data Layer class is where all db queries will be made.
    """
    def __init__(self, mysql):
        self.mysql = mysql
        self.queryManager = QueryManager()

    #User DataLayer
    """
    Login
    Parameters: username (String), password (String)
    Description: Fetch the user with username and password
    Return: User
    """
    def login(self, username, password):
        # Check if User exists using MySQL
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute(self.queryManager.login(), (username, password))
        # Fetch one record and return result
        return cursor.fetchone()

    """
    getUserByUsername
    Parameters: username (String)
    Description: Fetch the user with username
    Return: User
    """
    def getUserByUsername(self, username):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(self.queryManager.getUserByUsername(), (username,))
        # Fetch one record and return result
        return cursor.fetchone()

    """
    Register
    Parameters: user(User Model)
    Description: Insert user to db
    Return: _
    """
    def register(self, user):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(self.queryManager.register(), (user.username, user.email, 
            user.password, user.first_name, user.last_name, user.role))
        #Execute command
        self.mysql.connection.commit()
        
    """
    Update Role
    Parameters: userId, role
    Description: Update the user role
    Return: _
    """
    def updateRole(self, userId, role):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(self.queryManager.updateRole(), (role, userId))
        #Execute command
        self.mysql.connection.commit()

    """
    Register Business
    Parameters: business(Business Model)
    Description: Insert business to db
    Return: _
    """
    #Business Datalayer
    def registerBusiness(self, business):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(self.queryManager.registerBusiness(), (business.business_name, 
        business.address, business.city, business.zip_code,business.business_email,
        business.business_phone, business.max_capacity, business.business_ownerId, business.serviceId))
        #Execute command
        self.mysql.connection.commit()

    
    