from math import *
x = float(input())

if -4 <= x and x < 0:
	a = sqrt(abs(x))
	print(round(a , 4))
elif 0 <= x and x <= 4:
	a = sqrt(x) 
	print(round(a , 4))
else:
	print('entrada invalida')