from math import *

x = float(input("Digite um numero: "))
k = int(input("Digite um numero inteiro: "))

c = 0
a = 0

while(a < k):
	
	c = c + (1 + ((x**(2*k))/factorial(2*k)))
	a = a + 1
	
print(round(c, 8))
