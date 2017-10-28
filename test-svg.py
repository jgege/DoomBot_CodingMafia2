from svgpathtools import svg2paths, svg2paths2, wsvg
from bresenham import bresenham
import numpy as np

paths, attributes, svg_attributes = svg2paths2('../rooms/E1M1.svg')

size = svg_attributes['viewBox'].split(" ")
width = int(size[2]) + 1
height = int(size[3]) + 1

mapMatrix = [[0] * height for i in range(width)]

for path in attributes:
    isWall = path['stroke-width'] == '10'
    points = bresenham(int(path['x1']), int(path['y1']), int(path['x2']), int(path['y2']))
    for pt in points:
        if isWall:
            mapMatrix[pt[0]][pt[1]] = 2
        else:
            mapMatrix[pt[0]][pt[1]] = 1

s = ""
for i in range(len(mapMatrix)):
    for j in range(len(mapMatrix[i])):
        s += str(mapMatrix[i][j])
    print s
    s = ""
