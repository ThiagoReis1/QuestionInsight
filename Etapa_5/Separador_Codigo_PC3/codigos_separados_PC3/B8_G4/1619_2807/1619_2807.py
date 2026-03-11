from numpy import *

y= array(eval(input()))
x= array(eval(input()))

z = arange(size(x))

i = 0

while(i < size(x)):
	if(x[i] == "QUENTE"):
		z[i] = y[i] * 90
	elif(x[i] == "MORNO"):
		z[i] = y[i] * 45
	elif(x[i] == "FRIO"):
		z[i] = y[i] * 0
	i += 1
	
p = sum(z)

p = p * 0.005

print(round(p, 2))