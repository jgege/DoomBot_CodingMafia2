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
        print "MoveRatio: " + str(self.mvToCoordRatio)
        return self.mvToCoordRatio
    
    def calibrateTurning(self):
        """
        degree = 90
        startInfo = self.api.player.getInfo()
        self.api.player.turnLeft(degree)
        time.sleep(4)
        self.refreshSelfInfo()
        endInfo = self.info
        angleDiff = endInfo['angle'] - startInfo['angle']
        
        self.rotateRatio = float(angleDiff) / float(degree)        
        print "TurnRatio: " + str(self.rotateRatio)
"""
        self.rotateRatio = 3.00789474
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
        
        playerAngle = self.info['angle']%360
        print "PA: " + str(playerAngle) + " oPA: " + str(self.info['angle'])
        print "A: " + str(angle%360) + " oPA: " + str(angle)
        angle %= 360
        
        if ((playerAngle+180) < angle or playerAngle > angle):
            print "Turn right..."
            self.turnRight(abs(angle-360-playerAngle)%360)
        else:
            print "Turn left..."
            self.turnLeft((360-playerAngle+angle)%360)
        
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        print "setAngle: " + str(angle)
        
        if (angle == 0):
            self.setAngleToZero()
            return;
        
        #print "PA: " + str(self.info['angle'])
        playerAngle = self.info['angle'] - 180 # -180;180
        #print "PA-180: " + str(playerAngle)
        #print "angle " + str(angle)
        angle -= 180 # -180;180
        #print "angle-180 " + str(angle)
        angleDistance = (playerAngle) - (angle)
        print "AD: " + str(angleDistance+180)
        print "PA: " + str(playerAngle+180)
        #print "AD: " + str(angleDistance)
        # 50 - 10
        # 10 - 50
        
        if (angleDistance > 0):
            self.turnLeft(angleDistance+180)
        else:
            self.turnRight(angleDistance+180)

    def calcAbsDistance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    
    def calcDistanceFromObject(self, objX, objY):
        self.refreshSelfInfo()
        return self.calcAbsDistance(self.info['position']['x'], self.info['position']['y'], objX, objY)
    
    def moveForward(self, coords):
        self.api.player.moveForward(self.mvToCoordRatio*coords/2)
    
    def moveBackward(self, coords):
        self.api.player.moveBackward(self.mvToCoordRatio*coords/2)
        
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
        self.setAngle(angle)

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
