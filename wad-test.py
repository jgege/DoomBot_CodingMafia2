from WADParser import Wad
from bresenham import bresenham
import time
from ApiWrapper import ApiWrapper
from Player import Player
import time

import struct

api = ApiWrapper("http://localhost:6001")
bot = Player(api)

start = (1051, -3650)
end = (3017, -4847)

def printAreaAroundPlayer(x,y,matrix):
    for i in range(x - 20, x + 20):
        s = ""
        for j in range(y - 30, y + 30):
            if i == x and j == y:
                s += 'I'
            else:
                if not i in matrix or not j in matrix[i]:
                    s+= '0'
                else:
                    s += str(matrix[i][j])
        print s

def findWalls(x,y,matrix):
    radius = 17
    s = ""
    for i in range (x-radius, x+radius):
        for j in range (y-radius, y+radius):
            if i in matrix and j in matrix[i] and matrix[i][j] == 2:
                if j < y:
                    s += "north "
                if j > y:
                    s += "south "
                if i < x:
                    s += "west"
                if i > x:
                    s += "east"
                print s
                s = ""


wad = Wad("doom1.wad")
lvl = wad.levels[0]

mapList = {}

for i in lvl.lines:
    isWall = i.is_one_sided()
    points = bresenham(lvl.vertices[i.a][0], lvl.vertices[i.a][1], lvl.vertices[i.b][0], lvl.vertices[i.b][1])
    for pt in points:
        if not pt[0] in mapList:
            mapList[pt[0]] = {}
        if isWall:
            mapList[pt[0]][pt[1]] = 2
        else:
            mapList[pt[0]][pt[1]] = 1



""" get mins and maxs
min = (0,0)
max = (0,-20000)
for i in mapList:
    if (min[0] > i):
        min = (i, min[1])
    if (max[0] < i):
        max = (i, max[1])
    for j in mapList[i]:
        if (min[1] > j):
            min = (min[0], j)
        if (max[1] < j):
            max = (max[0], j);

print min, max

divide = 12
for i in range(len(mapMatrix)):
    s = ""
    max = 0
    for j in range(len(mapMatrix[i])):
        if max < mapMatrix[i][j]:
            max = mapMatrix[i][j]
        if (j % divide == 0):
            s += str(max)
            max = 0
    print s
"""
"""
bot.refreshSelfInfo()
ppos = (int(bot.info['position']['x']), int(bot.info['position']['y']))
for i in range (80):
    bot.refreshSelfInfo()
    ppos = (int(bot.info['position']['x']), int(bot.info['position']['y']))
    printAreaAroundPlayer(ppos[0], ppos[1], mapList)
    #bot.moveForwardByCoords(20)
    findWalls(ppos[0], ppos[1], mapList)
    time.sleep(0.5)
"""
