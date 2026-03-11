from math import*
x = float(input())
if x >= -4 and x < 0:
	print(round((-x) ** 0.5 , 4))
elif x>= 0 and x <= 4:
	print(round(x ** 0.5 , 4))
else: print("entrada invalida")