from math import floor, log

n = int(input('Input: '))
print('r = ', floor(log(n, 2)) + 1)
print('Result (2^r) = ', 2**(floor(log(n, 2)) + 1))
