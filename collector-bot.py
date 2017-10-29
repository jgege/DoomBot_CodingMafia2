from MapGrid import MapGrid
from Player import Player
from ApiWrapper import ApiWrapper
import time

api = ApiWrapper("http://localhost:6001")
bot = Player(api)
buffs = bot.findBuffs()
mapGrid = MapGrid()

while (bot.collectClosestBuff(mapGrid)):
    continue

"""
for bf in buffs:
    bot.refreshSelfInfo()
    print "#####"
    print "# I'm going to collect a " + str(bf["type"]) + " at " + str(bf['position']['x']) + ":" + str(bf['position']['y']) + ". It is " + str(bf['distance']) + " distance from here."
    print "#####"
    start = (bot.x, bot.y)
    destX = int(bf['position']['x'])
    destY = int(bf['position']['y'])
    end = (int(destX), int(destY))
    #print start, end
    start = mapGrid.transformPos(start)
    end = mapGrid.transformPos(end)
    #print start, end
    foundPath = list(mapGrid.astar(start, end))
    
    for i in range(0, len(foundPath), 4):
        position = mapGrid.transformPosBack(foundPath[i])
        bot.moveTo(position[0], position[1])
        time.sleep(0.07)
    time.sleep(1)
    bot.use()
    time.sleep(0.5)
"""