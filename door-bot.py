from MapGrid import MapGrid
from Player import Player
from ApiWrapper import ApiWrapper
import time

api = ApiWrapper("http://localhost:6001")
bot = Player(api)
doors = api.world.getDoors()
mapGrid = MapGrid()

def avg(a,b):
    return (a+b)/2

def posInRadiusOfPos(p1, p2, r):
    p2 = (p2[0]-r, p2[0]+r, p2[1]-r, p2[0]+r)
    isInRadius = True
    if not p2[0] <= p1[0] <= p2[1]:
        isInRadius = False
    if not p2[2] <= p1[0] <= p2[3]:
        isInRadius = False
    return isInRadius


for door in doors:
    bot.refreshSelfInfo()
    start = (bot.x, bot.y)
    doorX = avg(door['line']['v1']['x'], door['line']['v2']['x'])
    doorY = avg(door['line']['v1']['y'], door['line']['v2']['y'])
    end = (int(doorX), int(doorY))
    #print end, mapGrid.transformPosBack(mapGrid.transformPos(end)), mapGrid.transformPos(end), (end[0] - start[0], end[1] - start[1])
    print start, end
    start = mapGrid.transformPos(start)
    end = mapGrid.transformPos(end)
    #print start, end
    foundPath = list(mapGrid.astar(start, end))
    reached = False
    #while not reached:
    #    reached = True
    for i in range(0, len(foundPath), 1):
        position = mapGrid.transformPosBack(foundPath[i])
        bot.moveTo(position[1], position[0])
        time.sleep(2)
        bot.refreshSelfInfo()
        start = (bot.x, bot.y)
        print start, position
        if not posInRadiusOfPos(start, position, 32):
            print "stuck", start, position
    time.sleep(1)
    bot.use()
    time.sleep(0.5)
