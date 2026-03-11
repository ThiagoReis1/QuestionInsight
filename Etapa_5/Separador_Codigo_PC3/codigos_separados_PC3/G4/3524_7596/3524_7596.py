from math import*
x = float(input("numero real: "))
cont = int(input("numero inteiro: "))
cosh = 0
k = 0

while(cont > 0):
	cosh = (x**k)/factorial(k) + cosh
	cont = cont - 1
	k = k + 2
print(round(cosh,8))