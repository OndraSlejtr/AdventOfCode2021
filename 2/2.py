filename = '2.txt'

with open(filename) as file:
    lines = file.readlines()

lines = [tuple(line.rstrip().split(' ')) for line in lines]

depth = 0
pos = 0
aim = 0

for cmd, distance in lines:
    match cmd:
        case 'forward':
            pos += int(distance)
            depth += aim * int(distance)
        case 'down':
            aim += int(distance)
        case 'up':
            aim -= int(distance)

print(depth * pos)