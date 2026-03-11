n = int(input("Número da série: "))

contador = 0
sinal = -1
PIn = 0

from math import *
while(contador < n):
	PIn = sinal * ((1 + contador) ** (1/2))/((2 * contador + 3) + 6)
	sinal = - sinal
	contador = contador + 1
	print(round(PIn, 5))