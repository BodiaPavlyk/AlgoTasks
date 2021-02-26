from math import ceil, sqrt

def check(number):
  exist = False
  for i in range(1, int(ceil(sqrt(number)))):
      for j in range(1, int(ceil(sqrt(number-i**2)))):
        third = number - i**2 - j**2
        if third > 0 and float(third**(1/2))%1 == 0:
          exist = True
          print(i, "^2 + ", j, "^2 + ", int(third**(1/2)), "^2")
  if not exist:
      return False
  else:
      return True


n = int(input('Input: '))
if not check(n):
  print("It`s impossible!")
