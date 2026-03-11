from math import *
x = float(input("valor de x: "))

if x <= -1 or x >= 1:
	funcao = sqrt(abs(x))
	print(round(funcao,2))
elif x == 0:
	print(round(x,2))
else:
	funcao = abs(x)
	print(round(funcao,2))
#elif x <=-1 and x >= 0 or x <= 0 and >= 1:
#	funcao = abs(x)
#	print(x)

