from dataclasses import dataclass
import numpy as np

@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    start: Point
    end: Point


filename = __file__.replace('py', 'txt')

with open(filename) as file:
    input = file.readlines()

lines = []

for line in input:
    points = [[coord for coord in point.split(',')]
              for point in line.rstrip().split(' -> ')]
    lines.append(
        Line(Point(int(points[0][0]), int(points[0][1])), Point(int(points[1][0]), int(points[1][1]))))

map = np.zeros((1000, 1000), dtype=int)

for line in lines:
    if line.start.x != line.end.x and line.start.y == line.end.y:

        coords = [line.start.x, line.end.x]
        for x in range(min(coords), max(coords) + 1):
            map[x][line.start.y] += 1

    elif line.start.y != line.end.y and line.start.x == line.end.x:

        coords = [line.start.y, line.end.y]
        for y in range(min(coords), max(coords) + 1):
            map[line.start.x][y] += 1

cnt = 0

for x in np.nditer(map):
   if x >= 2:
       cnt += 1

print(cnt)


