#------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# LARISSA SANTOS BRITO
# DATA: 28/08/2016
# OBJETIVO: Determinar o número de séries de um termo
#-------------------------------------------------------
from math import *

N = int(input("digite o numero de termos:"))

i = 1
total = (-1 ) / 9
x = 9

while (i != N):
		if (N % 2 != 0):
			i = i + 1
			total = total - ( i / x + 2)
		else: 
			i = i + 1
			total = total - (i / x + 2)
print (round(total, 5))