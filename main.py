import math

n = int(input('Input: '))

exist = False
for i in range(1, int(math.ceil(math.sqrt(n)))):
    for j in range(1, int(math.ceil(math.sqrt(n)))):
        third = n - i**2 - j**2
        if third > 0 and float(third**(1/2))%1 == 0:
            exist = True
            print(i, "^2 + ", j, "^2 + ", int(third**(1/2)), "^2")
if not exist:
    print("It`s impossible!")
