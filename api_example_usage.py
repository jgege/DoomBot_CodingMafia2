from ApiWrapper import ApiWrapper

api = ApiWrapper("localhost:6001")
print "Player: "
print api.player.getInfo()
print "PlayerS: "
print api.players.getInfo()
print "World: "
print api.world.getInfo()
