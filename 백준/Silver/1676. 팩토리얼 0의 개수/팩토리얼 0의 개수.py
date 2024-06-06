from math import factorial

fac = (str(factorial(int(input()))))

print(len(fac) - len(str(int(fac[::-1]))))
