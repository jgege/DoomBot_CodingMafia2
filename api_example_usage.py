from ApiWrapper import ApiWrapper
import time

api = ApiWrapper("http://localhost:6001")
print "Player: "
#print api.player.getInfo()
#print api.player.walkForward(25)
#print "PlayerS: "
#print api.players.getInfo()
#print "World: "
#print api.world.getInfo()

#api.player.moveForward(25)
#api.player.turnLeft(25)
#api.player.moveBackward(10)

print api.world.getObjects()
#print api.world.getDoors()

#print api.player.turnRightByAngle(45)
#time.sleep(1)
#api.player.turnRightByAngle(90)

#for x in range(0, 10):
#    api.player.shoot()
#    time.sleep(0.1)    
