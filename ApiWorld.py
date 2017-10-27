from ApiEndPoint import ApiEndPoint

class ApiWorld(ApiEndPoint):
    def __init__(self, connection):
        super(ApiWorld, self).__init__(connection)
        
    def getInfo(self):
        return super(ApiWorld, self).sendRequest("GET","/api/world")