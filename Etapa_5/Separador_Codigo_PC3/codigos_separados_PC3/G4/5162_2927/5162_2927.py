from math import*

a = float(input("metro quadrado: "))
b = float(input("comprimento: "))

qt = 3* (sqrt(3*(b**2))/2)
x = (a*qt)
print(int(x))