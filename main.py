import math

n = int(input('Input: '))

for i in range(1, int(math.ceil(math.sqrt(n)))):
    for j in range(1, int( math.ceil(math.sqrt(n-i**2)))):
        third = n - i**2 - j**2
        if third > 0 and float(third**(1/2))%1 == 0:
            print(i, "^2 + ", j, "^2 + ", int(third**(1/2)), "^2")
            exit(0)
print("It`s impossible!")