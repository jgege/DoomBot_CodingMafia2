import math
import time

class Player(object):
    def __init__(self, apiw):
        self.api = apiw
        self.refreshSelfInfo()
        self.mvToCoordRatio = None
        self.rotateRatio = None
        
        self.calibrateMovement()
        self.calibrateTurning()
        self.refreshSelfInfo()
        
    def calibrateMovement(self):
        startInfo = self.api.player.getInfo()
        self.api.player.moveForward(2)
        time.sleep(1)
        endInfo = self.api.player.getInfo()
        absDistance = self.calcAbsDistance(startInfo['position']['x'], startInfo['position']['y'], endInfo['position']['x'], endInfo['position']['y'])
        
        self.mvToCoordRatio = 2 / float(absDistance)
        print "MTCR: " + str(self.mvToCoordRatio)
        return self.mvToCoordRatio
    
    def calibrateTurning(self):
        degree = 45
        startInfo = self.api.player.getInfo()
        self.api.player.turnLeft(degree)
        time.sleep(2)
        self.refreshSelfInfo()
        endInfo = self.info
        angleDiff = abs(startInfo['angle'] - endInfo['angle'])
        
        self.rotateRatio = float(angleDiff) / float(degree)
        
        print "RR: " + str(self.rotateRatio)

        return self.rotateRatio
    
    def turnLeft(self, degree):
        if (self.rotateRatio > 0):
            degree /= self.rotateRatio
        self.api.player.turnLeft(degree)

    def turnRight(self, degree):
        if (self.rotateRatio > 0):
            degree /= self.rotateRatio
        self.api.player.turnRight(degree)

    def setAngleToZero(self):
        print self.info['angle']
        if (self.info['angle'] < 180):
            print "R" + str(self.info['angle'])
            self.turnRight(self.info['angle']) 
            return
        
        print "L" + str(360 - self.info['angle'])
        self.turnLeft(360 - self.info['angle'])

    def setAngle(self, angle):
        turnLeft = True
        oppositeAnglePoint = self.info['angle'] - 180
        if (oppositeAnglePoint < angle):
            turnLeft = False
            #oppositeAnglePoint += 360
        
        
        
        print self.info['angle']
        print angle
        
        if (self.info['angle'] < 180):
            print "R" + str(self.info['angle'])
            self.turnRight(self.info['angle']) 
            return
        
        print "L" + str(360 - self.info['angle'])
        self.turnLeft(360 - self.info['angle'])

    def calcAbsDistance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    
    def moveForwardByCoords(self, coords):
        self.api.player.moveForward(self.mvToCoordRatio*coords/2)
        
    def findTheClosestDoor(self):
        doorList = self.api.world.getDoors()
        closestDoor = None
        for door in doorList:
            if (closestDoor is None):
                closestDoor = door
            elif(closestDoor['distance'] > door['distance']) :
                closestDoor = door
                
        return closestDoor
    
    def findTheClosestBarrel(self):
        objectList = self.api.world.getObjects()
        closestBarrel = None
        for obj in objectList:
            if (obj['type'] == "Barrel"):
                if (closestBarrel is None):
                    closestBarrel = obj
                elif(closestBarrel['distance'] > obj['distance']) :
                    closestBarrel = obj
                
        return closestBarrel
    
    def canISee(self, objId):
        return self.api.world.isLos(self.info['id'], objId)

    def refreshSelfInfo(self):
        self.info = self.api.player.getInfo();

    def turnTowards(self, x, y):
        angle = math.degrees(math.atan2(y - self.info['position']['y'], x - self.info['position']['x']))
        self.turnToAbsAngleFast(angle)
        #self.api.player.turnLeft(angle)

    def turnToAbsAngleFast(self, angle):
        if ((self.info['angle'] + 180) % 360 > angle):
            self.turnLeft(angle)
        else:
            self.turnRight(angle)

"""
    
        
    
"""
