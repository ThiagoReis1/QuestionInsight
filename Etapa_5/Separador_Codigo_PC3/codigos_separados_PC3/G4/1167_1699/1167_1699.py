#-------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS 
# ANA REBECA CAVALCANTE EVANGELISTA 
# MATRICULA: 21456290
# DATA: 28/07/2016
# OBJETIVO: Valor da serie.
#-------------------------------------------

from math import *

N = int(input("Digite o valor de termos: "))

i = 1
total = ( (-1 ** 2) / 8 )
x = 8

while (i != N):
	if (N % 2 == 0):
		i = i + 1
		total = total + ( i ** 2 / (x + 2) )
	else:
		i = i + 1 * -1
		total = total + ( (i ** 2) / (x + 2) )
		
print (round(total, 11))