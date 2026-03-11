from math import*
x = float(input("Digite um numero: "))

if(x <= 0):
	x = 0
	print(round(x,4))
elif (0 < x<=1):
	x = 1
	print(round(x,4))
elif (1 < x <= 2 ):
	a = sqrt(x)
	print(round(a,4))
else:
	b = x**(1/3)
	print(round(b,4))
	