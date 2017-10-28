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
        """
        degree = 45
        startInfo = self.api.player.getInfo()
        self.api.player.turnLeft(degree)
        time.sleep(2)
        self.refreshSelfInfo()
        endInfo = self.info
        angleDiff = abs(startInfo['angle'] - endInfo['angle'])
        
        self.rotateRatio = float(angleDiff) / float(degree)
        
        print "RR: " + str(self.rotateRatio)
"""
        self.rotateRatio = math.pi
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
        print "Current angle: " + str(self.info['angle'])
        if (self.info['angle'] < 180):
            print "R" + str(self.info['angle'])
            self.turnRight(self.info['angle']) 
            return
        
        print "L" + str(360 - self.info['angle'])
        self.turnLeft(360 - self.info['angle'])

    def setAngle(self, angle):
        self.refreshSelfInfo()
        time.sleep(1)
        
        if (angle == 0):
            self.setAngleToZero()
            return;
        
        playerAngle = self.info['angle']
        
        if ((playerAngle + 180) > angle):
            self.turnLeft((playerAngle+360-angle)%360)
        else:
            self.turnRight(angle-playerAngle)
        
        """
        print "Angle: " + str(angle)
        provisional = angle - self.info['angle']
        print "selfAngle: " + str(self.info['angle'])
        print "Provisional: " + str(provisional)
        
        if (self.info['angle'] < 180 and self.info['angle'] > angle):
            print "Turn to left (#1) " + (str(self.info['angle']-angle))
            self.turnLeft(self.info['angle']-angle)
            return
        
        if (provisional < 0):
            provisional += 360
            
            print "Corrected provisonal: " + str(provisional)
            
        if (provisional > 180):
            print "Turn right by " + str(provisional)
            self.turnRight(provisional)
            return
        
        print "Turn left by " + str(provisional)
        self.turnLeft(provisional)
        self.refreshSelfInfo()
"""
    def calcAbsDistance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    
    def calcDistanceFromObject(self, objX, objY):
        self.refreshSelfInfo()
        return self.calcAbsDistance(self.info['position']['x'], self.info['position']['y'], objX, objY)
    
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
        self.refreshSelfInfo()
        # calculates the degree between two points (it doesn't care about what is their current rotation)
        angle = math.degrees(math.atan2(y - self.info['position']['y'], x - self.info['position']['x']))
        print "turnTowards angle: " + str(angle)
        self.setAngle(abs(angle))

    def turnToAbsAngleFast(self, angle):
        if ((self.info['angle'] + 180) % 360 > angle):
            self.turnLeft(angle)
        else:
            self.turnRight(angle)

    def shoot(self):
        self.api.player.shoot()
        
    def burstFire(self, shots):
        for i in range(0,shots):
            self.shoot()
            time.sleep(0.1)
            
    def findObject(self, objectId):
        return self.api.world.getObjectById(objectId)
"""
    
        
    
"""
