from MapGrid import MapGrid
from Player import Player
from ApiWrapper import ApiWrapper
from bresenham import bresenham
import time

def avg(a,b):
    return (a+b)/2

api = ApiWrapper("http://localhost:6001")
bot = Player(api)
mapGrid = MapGrid()
doors = api.world.getDoors()
del doors[1]

gridCopy = mapGrid.grid

pSymbols = ("A","B","C","D","E","F","G","H")
dSymbols = ("Y", "X", "V", "N", "M")
pathCounter = 0
doorCounter = 0
for door in doors:
	print door
	bot.refreshSelfInfo()
	start = (bot.x, bot.y)
	doorX = avg(door['line']['v1']['x'], door['line']['v2']['x'])
	doorY = avg(door['line']['v1']['y'], door['line']['v2']['y'])
	end = (int(doorX), int(doorY))
	start = mapGrid.transformPos(start)
	end = mapGrid.transformPos(end)
	foundPath = list(mapGrid.astar(start, end))
	
	for path in foundPath:
		gridCopy[path[1]][path[0]] = pSymbols[pathCounter]
		
	# put doors to the map
	doorLine = bresenham(door['line']['v1']['x'],  door['line']['v1']['y'], door['line']['v2']['x'], door['line']['v2']['y'])
	for dPoint in doorLine:
		transformedDPoint = mapGrid.transformPos((dPoint[0], dPoint[1]))
		gridCopy[transformedDPoint[1]][transformedDPoint[0]] = dSymbols[doorCounter] 
	
	doorCounter += 1
	pathCounter += 1

for line in mapGrid.grid:
	s = ""
	for field in line:
		s += str(field)
	print s
	