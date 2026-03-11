from math import*
x = float(input())

if x >= -4 and x < 0:
	a = abs(x)**(1/2)
	print(round(a,4))
elif x >= 0 and x <= 4:
	a = x ** (1/2)
	print(round(a,4))
else:
	print('entrada invalida')

