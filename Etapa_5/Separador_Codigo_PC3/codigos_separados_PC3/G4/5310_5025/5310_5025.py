x = float(input("valor de x:"))
k = int(input())
s = 0
cont = 0
from math import *
while (cont<k):
	s = s + x / factorial(2*cont + 1)
	cont = cont + 1
print(round(s,8))