import math

n = int(input('Input: '))
print('r = ', math.floor(math.log(n, 2)) + 1)
print('Result (2^r) = ', 2**(math.floor(math.log(n, 2)) + 1))
