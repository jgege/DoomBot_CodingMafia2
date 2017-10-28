from ApiEndPoint import ApiEndPoint

class ApiWorld(ApiEndPoint):
    def __init__(self, host):
        self.host = host

    def getInfo(self):
        return super(ApiWorld, self).get("/api/world")

    def getDoors(self):
        return super(ApiWorld, self).get("/api/world/doors")

    def getDoorById(self, doorId):
        return super(ApiWorld, self).get("/api/world/doors/" + doorId)
    
    def moveTest(self, objectId, x, y):        
        payload = {'id': objectId, 'x': x, 'y': y}
        return super(ApiWorld, self).get("/api/world/movetest", payload)
    
    def getObjects(self):
        return super(ApiWorld, self).get("/api/world/objects")
    
    def getObjectById(self, objectId):
        return super(ApiWorld, self).get("/api/world/objects/" + str(objectId))
    
    def isLos(self, objectId1, objectId2):
        return super(ApiWorld, self).get("/api/world/los/" + str(objectId1) + "/" + str(objectId2))
        