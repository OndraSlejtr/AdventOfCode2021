import numpy as np

filename = __file__.replace('py', 'txt')

with open(filename) as file:
    lines = file.readlines()

gamma_occurence = [0] * len(lines[0].rstrip())
binary_len = len(lines)

for line in lines:
    gamma_occurence = np.add(
        gamma_occurence, [int(bit) for bit in line.rstrip()])

gamma_bits = [int(bit > binary_len/2) for bit in gamma_occurence]


def bitarray_to_int(array):
    return int(''.join('01'[i] for i in array), 2)


gamma = bitarray_to_int(gamma_bits)
epsilon = bitarray_to_int([n ^ 1 for n in gamma_bits])

print(gamma_occurence)
print(gamma)
print(epsilon)

print(gamma * epsilon)
