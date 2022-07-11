filename = '1.txt'

with open(filename) as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]


    count = 0

    for idx, val in enumerate(lines):
        if idx == 0:
            continue
        if lines[idx] > lines[idx-1]:
            count += 1
        else:
            print(f'{lines[idx]} <= {lines[idx-1]}')

    print(count)

