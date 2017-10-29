from WADParser import Wad
from bresenham import bresenham
from astar import AStar
from ApiWrapper import ApiWrapper
from ApiWorld import ApiWorld
import math

class MapGrid(AStar):
    def __init__(self):
        api = ApiWrapper("http://localhost:6001")
        self.apiWorld = ApiWorld(api)
        wad = Wad("doom1.wad")
        lvl = wad.levels[0]
        self.grid = None

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
        self.sampleSize = 16
        width = int((self.max[0] - self.min[0]) / self.sampleSize)
        height = int((self.max[1] - self.min[1]) / self.sampleSize)
        #print "HW:", width, height

        self.grid  = [[0 for x in range(width+1)] for y in range(height+1)]
        print len(self.grid), len(self.grid[0])
        print (self.max[0] - self.min[0], self.max[1] - self.min[1])

        # fill up the self.grid
        #for yC in range(len(self.grid)):
        #    for xC in range(len(self.grid[0])):
        #        self.grid[yC][xC] = 0

        for i in lvl.lines:
            isWall = i.is_one_sided()
            points = bresenham(lvl.vertices[i.a][0], lvl.vertices[i.a][1], lvl.vertices[i.b][0], lvl.vertices[i.b][1])
            for pt in points:
                x = int((pt[0] + abs(self.min[0]))/self.sampleSize)
                y = int((pt[1] + abs(self.min[1]))/self.sampleSize)
                try:
                    if isWall:
                        self.grid[y][x] = 2
                    else:
                        self.grid[y][x] = 1
                except Exception, e:
                    print e.message
                    #print self.grid
                    print x,y,width,height
                    exit()

        for yC in range(0, len(self.grid)):
            s = ""
            for xC in range(0, len(self.grid[0])):
                s += str(self.grid[yC][xC])
            #print s

    def transformPos(self, id):
        x = int((id[0] + abs(self.min[0]))/self.sampleSize)
        y = int((id[1] + abs(self.min[1]))/self.sampleSize)
        return x, y

    def transformPosBack(self, id):
        x = id[0]*self.sampleSize + self.min[0]
        y = id[1]*self.sampleSize + self.min[1]
        return x, y

    def in_bounds(self, id):
        (x, y) = id
        #print id, (len(self.grid), len(self.grid[0]))
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

    def passable(self, id):
        (x, y) = id
        return self.grid[x][y] != 1

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def heuristic_cost_estimate(self, n1, n2):
        """computes the 'direct' distance between two (x,y) tuples"""
        (x1, y1) = self.transformPos(n1)
        (x2, y2) = self.transformPos(n2)
        #print len(self.grid), len(self.grid[0]), (x1, y1), (x2, y2)
        return math.hypot(x2 - x1, y2 - y1)

    def distance_between(self, n1, n2):
        #print n1, self.transformPos(n1), n2
        """this method always returns 1, as two 'neighbors' are always adajcent"""
        return 1

    def is_goal_reached(self, current, goal):
        #print "goal", current, goal
        return current[0] == goal[0] and current[1] == goal[1]
