x = float(input("qual o valor de x?: "))
total = 0

from math import *

if ( -1000 <= x < -2):
	total =  (-1/(x+2))
	print(round(total, 4))
else:
	if ( 2 < x <= 1000):
		total= ( 1/(x-2))
		print(round(total, 4))
	else:
		print("entrada invalida")