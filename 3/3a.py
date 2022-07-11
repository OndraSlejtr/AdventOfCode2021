import numpy as np


def bitarray_to_int(array):
    return int(''.join('01'[i] for i in array), 2)


def count_bit_occurance(readings):
    bit_occurence = [0] * len(readings[0].rstrip())
    reading_count = len(readings)

    for reading in readings:
        bit_occurence = np.add(
            bit_occurence, [int(bit) for bit in reading.rstrip()])

    return (bit_occurence, reading_count)


filename = __file__.replace('py', 'txt')

with open(filename) as file:
    readings = [line.rstrip() for line in file.readlines()]


oxygen_readings = readings
co_readings = readings


def reading_check(bit_pos, line, oxygen_reading, pref_value, occurance_comparator):
    occurence, reading_count = count_bit_occurance(oxygen_reading)

    common = int(occurence[bit_pos])
    current = int(line[bit_pos])

    if common == reading_count/2:
        return current == pref_value
    return current == int(occurance_comparator(common, reading_count / 2))


def oxygen_check(bit_pos, line, oxygen_reading):
    return reading_check(bit_pos, line, oxygen_reading, 1, lambda x, y: x > y)


def co_check(bit_pos, line, oxygen_reading):
    return reading_check(bit_pos, line, oxygen_reading, 0, lambda x, y: x < y)


for bit_pos in range(len(readings[0])):
    oxygen_readings = [reading for reading in oxygen_readings if oxygen_check(
        bit_pos, reading, oxygen_readings)]
    if len(oxygen_readings) == 1:
        break

for bit_pos in range(len(readings[0])):
    co_readings = [line for line in co_readings if co_check(
        bit_pos, line, co_readings)]
    if len(co_readings) == 1:
        break

print(oxygen_readings)
print(co_readings)

print(int(oxygen_readings[0], base=2) * int(co_readings[0], base=2))
