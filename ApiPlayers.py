from ApiEndPoint import ApiEndPoint

class ApiPlayers(ApiEndPoint):
    def __init__(self, connection):
        super(ApiPlayers, self).__init__(connection)
        
    def getInfo(self):
        return super(ApiPlayers, self).sendRequest("GET","/api/players")