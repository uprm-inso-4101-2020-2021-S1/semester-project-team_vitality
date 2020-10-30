#All queries used in application will be here
class QueryManager(object):
    """
    QueryManager class will have all query strings

    %s will be the parameters passed in order
    """
    def __init__(self):
        pass
        
    #User Queries
    def login(self):
        return """
        SELECT * FROM users 
        WHERE username = %s AND password = %s
        """
    
    def getUserByUsername(self):
        return """
        SELECT * FROM users WHERE username = %s
        """

    def register(self):
        return """
        INSERT INTO users VALUES (NULL, %s, %s, %s, %s, %s, %s)
        """
    
    def updateRole(self):
        return """
        UPDATE `sql9372928`.`users` SET `role` = %s WHERE (`userId` = '%s');
        """

    #Business Queries
    def registerBusiness(self):
        return """
        INSERT INTO businesses VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)
        """