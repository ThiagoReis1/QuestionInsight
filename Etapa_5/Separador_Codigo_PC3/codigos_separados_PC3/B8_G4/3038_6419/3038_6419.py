from math import*
x =  float(input("Digite o valor  de x: "))

if (x <= -1) or (x >= 1):
	fx = sqrt(abs(x))
	print(round(fx, 2))
elif (x > -1) and (x > 0):
	fx = abs(x)
	print(round(fx, 2))
elif (x == 0):
	fx  = 0
	print(round(fx, 2))