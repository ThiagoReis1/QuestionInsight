from math import *
x = float(input("Qual o valor de x: "))

if -4 <= x and x < 0:
	fx = sqrt(abs(x))
	print(round(fx, 4))
elif 0 <= x and x <= 4:
	fx = sqrt(x)
	print(round(fx, 4))
else:
	print("entrada invalida")
