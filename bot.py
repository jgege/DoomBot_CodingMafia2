from Player import Player
from ApiWrapper import ApiWrapper
import time

api = ApiWrapper("http://localhost:6001")
bot = Player(api)
#bot.doRotateRationTest()

#bot.setAngle(70)

print bot.api.world.getObjects()

while bot.selfBuff():
    continue


# SHOOTABLE


"""
while bot.destroyAllEnemies():
    print "I'm looking for enemies."
    if (bot.checkHealth() == False):
        print "I have to defend myself."
        bot.defend()
    continue
"""
"""
bot.refreshSelfInfo()
print bot.info['angle']

for i in range(0, 360, 45):
    print "setAngle: " + str(i)
    bot.setAngle(i)
    time.sleep(4)
    bot.refreshSelfInfo()
    print bot.info['angle']
   """ 
"""    
while True:
    bot.setAngle()
    #bot.setAngleToZero()
    time.sleep(10)
    bot.refreshSelfInfo()
    print bot.info['angle']
"""


"""
bot.refreshSelfInfo()
print "botpy CA:" + str(bot.info['angle'])
print "Set angle to: 90" 
bot.setAngle(90)
time.sleep(5)
bot.refreshSelfInfo()
print "botpy CA:" + str(bot.info['angle'])
print "Set angle to: 270"
bot.setAngle(270)
time.sleep(5)
bot.refreshSelfInfo()
print "botpy CA:" + str(bot.info['angle'])
print "Set angle to: 0"
bot.setAngle(0)
time.sleep(5)
bot.refreshSelfInfo()
print "botpy CA:" + str(bot.info['angle'])
"""
"""bot.setAngleToZero()
time.sleep(5)
bot.refreshSelfInfo()
print bot.info['angle']

bot.setAngle(270)
time.sleep(3)
bot.refreshSelfInfo()
print bot.info['angle']

bot.setAngle(0)
time.sleep(3)
bot.refreshSelfInfo()
print bot.info['angle']
"""
#print bot.goToTheClosestDoor()
#print bot.canIReach(bot.info['position']['x']+1, bot.info['position']['y'])
#print bot.info

#bot.turnLeftBy(90)
#bot.refreshSelfInfo()
#bot.turnRightBy(90)

#bot.turnLeftAbs(0)
"""
barrel = bot.findTheClosestBarrel()
if (barrel is not None and bot.canISee(barrel['id'])):
    print barrel
    bot.turnTowards(barrel['position']['x'], barrel['position']['y'])
    time.sleep(4)
    bot.moveForwardByCoords(barrel['distance'])
    time.sleep(4)
    barrel = bot.findObject(barrel['id'])
    print "WUT"
    print barrel
    if (barrel is not None):
        bot.moveForwardByCoords(bot.calcDistanceFromObject(barrel['position']['x'], barrel['position']['y'])-150)
        time.sleep(3)
        bot.turnTowards(barrel['position']['x'], barrel['position']['y'])
    
else:
    if (barrel is None):
        print "No barrel found"
    else:
        print "I can not see that barrel"
"""
def moveTest(bot):
    bot.doMoveTest()

    time.sleep(1)
    
    bot.refreshSelfInfo()
    x1 = bot.info['position']['x']
    y1 = bot.info['position']['y']
    print str(x1) + ';' + str(y1)
    
    bot.moveForwardByCoords(100)
    
    time.sleep(1)
    
    bot.refreshSelfInfo()
    x2 = bot.info['position']['x']
    y2 = bot.info['position']['y']
    print str(x2) + ';' + str(y2)
    
    
    print bot.calcAbsDistance(x1, y1, x2, y2)

def turnTest2(bot):
    print bot.doRotateRationTest()

def turnTest(bot):
    bot.refreshSelfInfo()
    print bot.info['angle']
    bot.turnToAbsAngleFast(100)
    time.sleep(2)
    bot.refreshSelfInfo()
    print bot.info['angle']