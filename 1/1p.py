filename = '1p.txt'

with open(filename) as file:
    lines = file.readlines()

lines = [int(line.rstrip()) for line in lines]

increase = 0

for a, b in zip(lines[:-2], lines[3:]):
    if a < b:
        increase += 1

print(increase)


[zip(lines[1:], lines[:-1])]
