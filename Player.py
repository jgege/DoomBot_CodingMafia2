class Player(object):
    def __init__(self, apiw):
        self.api = apiw
        
    def goToTheClosestDoor(self):
        doorList = self.api.world.getDoors()
        closestDoor = None
        for door in doorList:
            if (closestDoor is None):
                closestDoor = door
            elif(closestDoor['distance'] > door['distance']) :
                closestDoor = door
                
        print closestDoor
                