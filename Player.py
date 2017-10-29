import math
import time

class Player(object):
    def __init__(self, apiw):
        self.api = apiw
        self.refreshSelfInfo()
        self.mvToCoordRatio = None
        self.rotateRatio = None
        self.prevHealth = None
        self.enemyObjectList = ("ARACHNOTRON", "ARCH-VILE", "BARON OF HELL", "CACODEMON", "CHAINGUNNER", "COMMANDER KEEN", "CYBERDEMON", "DEMON", "FORMER HUMAN TROOPER", "FORMER HUMAN SERGEANT", "HELL KNIGHT", "IMP", "LOST SOUL", "MANCUBUS", "PAIN ELEMENTAL", "REVENANT", "SPECTRE", "SPIDER MASTERMIND", "WOLFENSTEIN SS")
        self.powerupsList = ("BACKPACK", "BLUE ARMOR", "GREEN ARMOR", "MEDIKIT", "RADIATION SUIT", "STIMPACK", "Health Potion +1% health", "Green armor 100%", "Spirit Armor +1% armor", "Blue armor 200%", "Health Potion +1% health")
        self.weaponsList = ("BFG", "CHAINGUN", "CHAINSAW", "PLASMA RIFLE", "ROCKET LAUNCHER", "SHOTGUN", "SUPER SHOTGUN")

        self.calibrateMovement()
        self.calibrateTurning()
        self.refreshSelfInfo()

    def calibrateMovement(self):
        startInfo = self.api.player.getInfo()
        self.api.player.moveForward(2)
        time.sleep(1)
        endInfo = self.api.player.getInfo()
        absDistance = self.calcAbsDistance(startInfo['position']['x'], startInfo['position']['y'], endInfo['position']['x'], endInfo['position']['y'])

        self.mvToCoordRatio = 1
        if (absDistance > 0):
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


    def calcAbsDistance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    def moveTo(self, x, y):
        self.turnTowards(x, y)
        time.sleep(1.25)
        dist = self.calcDistanceFromObject(x, y)
        self.moveForward(dist)

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

    def findClosestObjectFromType(self, objType):
        objectList = self.api.world.getObjects()
        closestObj = None
        #print objType
        for obj in objectList:
            fitsType = (((type(objType) is list or type(objType) is tuple) and (obj['type'] in objType)) or obj['type'] == objType)
            if (fitsType and self.canISee(obj['id'])): # and obj['health'] >= 0
                if (closestObj is None):
                    closestObj = obj
                elif(closestObj['distance'] > obj['distance']) :
                    closestObj = obj

        return closestObj

    def findSolidObjects(self):
        objectList = self.api.world.getObjects()
        returnList = []
        flag = "MF_SOLID"
        for obj in objectList:
            fitsType = flag in obj['flags'] and not obj['type'] in self.enemyObjectList
            if (fitsType):
                returnList.append(obj)

        returnList.sort(key=lambda x: x['distance'])
        return returnList

    def findBuffs(self):
        objectList = self.api.world.getObjects()
        returnList = []
        objType = self.weaponsList+self.powerupsList

        for obj in objectList:
            fitsType = (((type(objType) is list or type(objType) is tuple) and (obj['type'] in objType)) or obj['type'] == objType)
            if (fitsType):
                returnList.append(obj)

        returnList.sort(key=lambda x: x['distance'])

        return returnList

    def findTheClosestBarrel(self):
        return self.findClosestObjectFromType("Barrel")

    def canISee(self, objId):
        return self.api.world.isLos(self.info['id'], objId)

    def refreshSelfInfo(self):
        self.info = self.api.player.getInfo();
        self.x = int(self.info['position']['x'])
        self.y = int(self.info['position']['y'])

    def turnTowards(self, x, y):
        self.refreshSelfInfo()
        # calculates the degree between two points (it doesn't care about what is their current rotation)
        angle = self.returnObjectPlayerAngle(x, y)
        print "turnTowards angle: " + str(angle)
        self.setAngle(angle)

    def returnObjectPlayerAngle(self, x, y):
        return math.degrees(math.atan2(y - self.info['position']['y'], x - self.info['position']['x']))

    def shoot(self):
        self.api.player.shoot()

    def burstFire(self, shots):
        for i in range(0,shots):
            self.shoot()
            time.sleep(0.1)

    def findObject(self, objectId):
        return self.api.world.getObjectById(objectId)

    def destroyAllEnemies(self):
        self.refreshSelfInfo()
        enemy = self.findClosestObjectFromType(self.enemyObjectList)
        if (enemy is None):
            return False
        #print enemy

        self.moveCloseToObject(enemy, 0, 750)

        if (self.canISee(enemy['id'])):
            print "I can see it."
            if (self.isObjectInRightAngle(enemy['id'])):
                print "I can shoot it."
                self.burstFire(10)
            else:
                print "I can't shoot it yet."
        else:
            print "I can't see it yet."
        return True

    def destroyClosestBarrel(self):
        self.refreshSelfInfo()
        barrel = self.findTheClosestBarrel()
        if (barrel is None):
            return False
        print barrel

        self.moveCloseToObject(barrel, 100, 300)

        if (self.canISee(barrel['id'])):
            print "I can see it!"
            if (self.isObjectInRightAngle(barrel['id'])):
                print "I can shoot it!"
                self.burstFire(3)
            else:
                print "I can't shoot it yet!"
        else:
            print "I can't see it yet"
        return True

    def isObjectInRightAngle(self, objectId):
        object = self.findObject(objectId)

        self.refreshSelfInfo()
        angleDiff = self.info['angle'] - self.returnObjectPlayerAngle(object['position']['x'], object['position']['y'])
        return (angleDiff <= 7.5 and angleDiff >= -7.5)

    def moveCloseToObject(self, obj, minDist, maxDist):
        self.refreshSelfInfo()
        if (self.isObjectInRightAngle(obj['id']) == False):
            self.turnTowards(obj['position']['x'], obj['position']['y'])
            time.sleep(1.5)
            self.refreshSelfInfo()

        if (self.closeEnoughToObject(obj, maxDist) == False):
            self.moveForward(obj['distance'] - maxDist)
        if (self.tooCloseToObject(obj, minDist)):
            self.moveBackward(minDist - obj['distance'])

        time.sleep(2)

    def closeEnoughToObject(self, obj, maxDist):
        return obj['distance'] < maxDist

    def tooCloseToObject(self, obj, minDist):
        return obj['distance'] < minDist

    def defend(self):
        enemy = self.findClosestObjectFromType(self.enemyObjectList)

        if enemy is None:
            return False

        self.turnTowards(enemy['position']['x'], enemy['position']['y'])
        time.sleep(0.25)
        self.burstFire(5)

        return True

    def checkHealth(self):
        self.refreshSelfInfo()
        if (self.prevHealth is not None):
            if(self.prevHealth > self.info['health']):
                self.prevHealth = self.info['health']
                return False

        self.prevHealth = self.info['health']
        return True

    def collectPowerups(self):
        self.refreshSelfInfo()
        buff = self.findClosestObjectFromType(self.powerupsList)
        if (buff is None):
            return False
        print buff

        self.moveCloseToObject(buff, 0, 20)
        return True

    def collectWeapons(self):
        self.refreshSelfInfo()
        buff = self.findClosestObjectFromType(self.weaponsList)
        if (buff is None):
            return False
        print buff

        self.moveCloseToObject(buff, 0, 20)
        return True

    def selfBuff(self):
        self.refreshSelfInfo()
        buff = self.findClosestObjectFromType(self.weaponsList+self.powerupsList)
        if (buff is None):
            return False
        print buff

        self.moveCloseToObject(buff, 0, 20)
        return True

    def findClosestBuff(self):
        self.refreshSelfInfo()
        buff = self.findClosestObjectFromType(self.weaponsList+self.powerupsList)
        if (buff is None):
            return False
        return buff

    def collectClosestBuff(self, mapGrid):
        buff = self.findClosestBuff()
        if (buff is None):
            return False

        start = (self.x, self.y)
        destX = int(buff['position']['x'])
        destY = int(buff['position']['y'])
        end = (int(destX), int(destY))
        start = mapGrid.transformPos(start)
        end = mapGrid.transformPos(end)
        foundPath = list(mapGrid.astar(start, end))

        for i in range(0, len(foundPath), 4):
            position = mapGrid.transformPosBack(foundPath[i])
            self.moveTo(position[0], position[1])
            time.sleep(0.07)

        return True

    def use (self):
        self.api.player.use()

    def avg(self, a,b):
        return (a+b)/2

"""
    def getDoorsOrderByDistance(self):
        orderedDoorList
        doorList = self.api.world.getDoors()
   """
