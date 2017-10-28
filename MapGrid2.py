from WADParser import Wad
from bresenham import bresenham
from astar import AStar
from ApiWrapper import ApiWrapper
from ApiWorld import ApiWorld
import math

class MapGrid(object):
    def __init__(self):
        api = ApiWrapper("http://localhost:6001")
        self.apiWorld = ApiWorld(api)
        wad = Wad("doom1.wad")
        lvl = wad.levels[0]
        grid = None

        self.min = (0,0)
        self.max = (0,-20000)
        for i in lvl.lines:
            points = [lvl.vertices[i.a], lvl.vertices[i.b]]
            for pt in points:
                if self.min[0] > pt[0]:
                    self.min = (pt[0], self.min[1])
                if self.max[0] < pt[0]:
                    self.max = (pt[0], self.max[1])
                if self.min[1] > pt[1]:
                    self.min = (self.min[0], pt[1])
                if self.max[1] < pt[1]:
                    self.max = (self.max[0], pt[1])

        #print self.min, self.max
        sampleSize = 25
        width = int((self.max[0] - self.min[0]) / sampleSize)
        height = int((self.max[1] - self.min[1]) / sampleSize)
        #print "HW:", width, height
        
        grid  = [[0 for x in range(width)] for y in range(height)]
        
        # fill up the grid
        #for yC in range(len(grid)):
        #    for xC in range(len(grid[0])):
        #        grid[yC][xC] = 0
        
        for i in lvl.lines:
            points = [lvl.vertices[i.a], lvl.vertices[i.b]]
            #print points
            isWall = i.is_one_sided()
            points = bresenham(lvl.vertices[i.a][0], lvl.vertices[i.a][1], lvl.vertices[i.b][0], lvl.vertices[i.b][1])
            for pt in points:
                x = int((pt[0] + abs(self.min[0]))/sampleSize)-1
                y = int((pt[1] + abs(self.min[1]))/sampleSize)-1
                try:
                    if isWall:
                        grid[y][x] = 2
                    else:
                        grid[y][x] = 1
                except Exception, e:
                    print e.message
                    print grid
                    print x,y,width,height
                    exit()
        
        for yC in range(0, len(grid)):
            s = ""
            for xC in range(0, len(grid[0])):
                s += str(grid[yC][xC])
            print s
        
