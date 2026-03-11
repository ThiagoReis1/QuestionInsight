from math import asin
from math import acos

x = float(input("Informe x: "))

if(-1<=x and x<(-1/2)):
	resp = asin(x)
	print(round(resp,2))
elif((-1/2)<=x and x<=(1/2)):
	resp = acos(x)
	print(round(resp,2))
elif((1/2)<x and x<=1):
	resp = asin(x)
	print(round(resp,2))
else:
	print("entrada invalida")