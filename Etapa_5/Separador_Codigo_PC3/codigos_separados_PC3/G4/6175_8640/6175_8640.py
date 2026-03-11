from math import*

x = float(input("leia o valor de x: "))

if (x>=-4 and x<0):
	f =  abs (x)**(1/2)
	print(round(f,4))
elif (( x >= 0) and (x <=4)):
	f = x**(1/2)
	print(round(f,4))
else:
	print("entrada invalida")

