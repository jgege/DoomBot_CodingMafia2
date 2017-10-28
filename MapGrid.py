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

        print self.min, self.max
        width = self.max[0] - self.min[0]
        height = self.max[1] - self.min[1]
        self.mapMatrix = [[0 for row in range(height+1)] for col in range(width+1)]
        for i in lvl.lines:
            isWall = i.is_one_sided()
            points = bresenham(lvl.vertices[i.a][0], lvl.vertices[i.a][1], lvl.vertices[i.b][0], lvl.vertices[i.b][1])
            for pt in points:
                x = pt[0] + abs(self.min[0])
                y = pt[1] + abs(self.min[1])
                print x,y
                if isWall:
                    self.mapMatrix[x][y] = 2
                else:
                    self.mapMatrix[x][y] = 1


        for i in range (width):
            s = ""
            for j in range (height):
                if self.mapMatrix[i][j] == 0:
                    s+= " "
                else:
                    s += str(self.mapMatrix[i][j])
            print s

        """
        self.mapList = {}
        for i in lvl.lines:
            isWall = i.is_one_sided()
            points = bresenham(lvl.vertices[i.a][0], lvl.vertices[i.a][1], lvl.vertices[i.b][0], lvl.vertices[i.b][1])
            for pt in points:
                if not pt[0] in self.mapList:
                    self.mapList[pt[0]] = {}
                if isWall:
                    self.mapList[pt[0]][pt[1]] = 2
                else:
                    self.mapList[pt[0]][pt[1]] = 1

        self.min = (0,0)
        self.max = (0,-20000)
        for i in self.mapList:
            if (self.min[0] > i):
                self.min = (i, self.min[1])
            if (self.max[0] < i):
                self.max = (i, self.max[1])
            for j in self.mapList[i]:
                if (self.min[1] > j):
                    self.min = (self.min[0], j)
                if (self.max[1] < j):
                    self.max = (self.max[0], j);


        scale = 1
        width = (self.max[0] - self.min[0])/scale
        height = (self.max[1] - self.min[1])/scale
        tmpMatrix = [[0 for row in range(height+1)] for col in range(width+1)]
        for i in range(self.max[0] - self.min[0]):
            maxVal = 0
            for j in range(self.max[1] - self.min[1]):
                realPos = (self.min[0] + i, self.min[1] + j)
                newPos = (i / scale, j / scale)
                value = self.get_list_value(realPos)
                if value != 0:
                    if maxVal < value:
                        maxVal = value
                    if j % scale == 0:
                        if tmpMatrix[newPos[0]][newPos[1]] < maxVal:
                            tmpMatrix[newPos[0]][newPos[1]] = maxVal
                            maxVal = 0

        print  tmpMatrix[0][0]
        for i in range (width):
            s = ""
            for j in range (height):
                if tmpMatrix[i][j] == 0:
                    s+= " "
                else:
                    s += str(tmpMatrix[i][j])
            print s

        self.minMini = (self.min[0]/scale, self.min[1]/scale)
        self.maxMini = (self.max[0]/scale, self.max[1]/scale)


        self.mapMiniList = {}
        maxVal = [0 for row in range(0, self.max[1]/scale - self.min[1]/scale)]
        for i in range (self.min[0], self.max[0]):
            for j in range (self.min[1], self.max[1]):
                maxValIndex = (self.max[1] - j) / scale
                value = self.get_list_value((i,j))
                if len(maxVal) > maxValIndex and maxVal[maxValIndex] < value:
                    maxVal[maxValIndex] = value
                if (i % scale == 0 and j % scale == 0 and len(maxVal) > maxValIndex and maxVal[maxValIndex] != 0):
                    if not i/scale in self.mapMiniList:
                        self.mapMiniList[i/scale] = {}
                    self.mapMiniList[i/scale][j/scale] = maxVal[maxValIndex]
                    maxVal[maxValIndex] = 0

        self.minMini = (self.min[0]/scale, self.min[1]/scale)
        self.maxMini = (self.max[0]/scale, self.max[1]/scale)


        for i in range (self.minMini[0], self.maxMini[0]):
            s = ""
            for j in range (self.minMini[1], self.maxMini[1]):
                if not i in self.mapMiniList or not j in self.mapMiniList[i]:
                    s+='0'
                else:
                    str(self.mapMiniList[i][j])
            print s
            s = ""
        """


    def get_list_value(self, id):
        (x, y) = id
        if not x in self.mapList or not y in self.mapList[x]:
            return 0
        return self.mapList[x][y]

    def in_bounds(self, id):
        (x, y) = id
        return self.min[0] <= x < self.max[0] and self.min[1] <= y < self.max[1]

    def passable(self, id):
        (x, y) = id
        if not x in self.mapList or not y in self.mapList[x]:
            return True
        return self.mapList[x][y] == 1

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def heuristic_cost_estimate(self, n1, n2):
        """computes the 'direct' distance between two (x,y) tuples"""
        (x1, y1) = n1
        (x2, y2) = n2
        #print n1, n2
        return math.hypot(x2 - x1, y2 - y1)

    def distance_between(self, n1, n2):
        """this method always returns 1, as two 'neighbors' are always adajcent"""
        return 1
