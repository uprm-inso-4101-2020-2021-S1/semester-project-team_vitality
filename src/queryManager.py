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
        SELECT * FROM user 
        WHERE username = %s AND password = %s
        """
    
    def getUserByUsername(self):
        return """
        SELECT * FROM user WHERE username = %s
        """

    def register(self):
        return """
        INSERT INTO user VALUES (NULL, %s, %s, %s, CURRENT_TIMESTAMP, %s, %s, %s)
        """
    
    def updateRole(self):
        return """
        UPDATE `TeamVitality`.`user` SET `role` = '%s' WHERE (`userId` = '%s');
        """

    #Business Queries
    def registerBusiness(self):
        return """
        INSERT INTO business VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)
        """