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

bot.refreshSelfInfo()
start = (bot.x, bot.y)
for door in doors:
    doorX = avg(door['line']['v1']['x'], door['line']['v2']['x'])
    doorY = avg(door['line']['v1']['y'], door['line']['v2']['y'])
    end = (int(doorX), int(doorY))
    print start, end
    start = mapGrid.transformPos(start)
    end = mapGrid.transformPos(end)
    print start, end
    foundPath = list(mapGrid.astar(start, end))
    for i in range(0, len(foundPath), 3):
        position = mapGrid.transformPosBack(foundPath[i])
        while bot.calcDistanceFromObject(position[0], position[1]) > 52:
            bot.use()
            while not bot.checkHealth():
                bot.defend()
                time.sleep(1)
            bot.moveTo(position[0], position[1])
            time.sleep(0.07)
    time.sleep(1)
    time.sleep(0.5)
    bot.refreshSelfInfo()
    start = (bot.x, bot.y)
    mapGrid = MapGrid()
