from math import*

x=float(input("digite o valor x: "))

if x <= 0:
	print(0)
elif x >0 and x <=1:
	print(1)
elif x >1 and x <=2:
	print(round(sqrt(x),4))
else:
	print(round(x**(1/3),4))