from MapGrid import MapGrid

#start
#(1055, -3608) (1536, -2496)
#(113, 78) (144, 148)

# second
#(1536, -2496) (2944, -3840)
#(144, 148) (232, 64)

start = (1055, -3608)
#start = (1536, -2496)
#end = (1536, -2496)
end = (1536, -2496)
#end = (2944, -3840)
#end = (1000, -3650)
mapGrid = MapGrid()
start = mapGrid.transformPos(start)
end = mapGrid.transformPos(end)
#print(start, end)
foundPath = list(mapGrid.astar(start, end))
mapGrid.printWithPath(foundPath)
#for i in range(0, len(foundPath), 2):
#    print mapGrid.transformPosBack(foundPath[i])
