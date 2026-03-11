from numpy import *

p = array(eval(input("digite o preco: ")))
a = 0
x = 0

for i in range(size(p)):
	if(p[i] > 180):
		a = p[i] + a
		x = x + 1
if(x == 0):
	print("0.0")
else:
	b = a / x
	print(round(b,2))
		
		