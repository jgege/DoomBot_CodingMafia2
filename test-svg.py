from MapGrid import MapGrid

start = (1051, -3650)
#end = (1000, -3650)
end = (1536, -2496)
mapGrid = MapGrid()
start = mapGrid.transformPos(start)
end = mapGrid.transformPos(end)
foundPath = list(mapGrid.astar(start, end))
for p in foundPath:
    print mapGrid.transformPosBack(p)
