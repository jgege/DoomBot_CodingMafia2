from ApiWrapper import ApiWrapper
import ast

def isWall(i):
    info = json.loads(i)
    #info[]
    return false;



api = ApiWrapper("http://localhost:6001")
print "Player: "
#print api.player.getInfo()
print api.player.walkForward(25)
print "PlayerS: "
print api.players.getInfo()
print "World: "
print api.world.getInfo()
