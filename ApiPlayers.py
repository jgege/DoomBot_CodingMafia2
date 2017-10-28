from ApiEndPoint import ApiEndPoint

class ApiPlayers(ApiEndPoint):
    def __init__(self, host):
        self.host = host
        
    def getInfo(self):
        return super(ApiPlayers, self).get("/api/players")
    
    def getPlayerInfo(self, playerId):
        return super(ApiPlayers, self).get("/api/players/"+playerId)