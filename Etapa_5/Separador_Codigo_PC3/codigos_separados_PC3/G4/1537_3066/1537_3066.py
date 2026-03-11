from math import *
numX = float(input("digite: "))
numK = int(input("digite: "))
#termo geral = numX ** cont / factorial(cont)
cont = 0
a = 0
while (cont < numK):
	a = a + ((numX ** cont) / factorial(cont))
	cont = cont + 1
print(round(a, 9))
	
