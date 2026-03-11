from numpy import*

compra = array(eval(input("v:")))
x = sum(compra)

if(x >= 80):
	x1 = x * 15//100
	y = x - x1


print(round(y, 2))	