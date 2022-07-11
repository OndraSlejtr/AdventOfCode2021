lines = [int(line.rstrip()) for line in open('1.txt').readlines()]
count = sum([int(a < b) for a, b in zip(lines[:-2], lines[3:])])
print(count)
