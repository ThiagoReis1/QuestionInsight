x = float(input("Numero real: "))
k = int(input("Numero int: "))
from math import *
i = 0
cont = 0
a = 1
while (i<k):
	termo = (x**a) / factorial (a)
	cont = cont + termo
	a = a+2
	i = i+1
print(round(cont,9))
	


