from math import*
x = int(input("numero real: "))
k = int(input("numero inteiro: "))
senh = (x**x)/factorial(x)
termos = 1
indice = 2
from math import*
while(termos<k):
	senh = senh + (x**(x + indice))/factorial(x + indice)
	termos = termos + 1
	x = x 
print(round(senh,9))