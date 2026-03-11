from math import *

n = int(input())
cont = 0
valor = 0
sinal = 1
den = 3

while(n>0):
	#print (den)
	sinal = sinal * (-1)
	cont = cont + 1
	valor = valor + sinal * sqrt(cont)/(6 + den)
	den = den + 2
	n = n-1

print (round(valor,5))