from numpy import *

# Todo número é substituído pelo dobro

#x = [3, 5, 0, 1, 2, 9]
x = array(eval(input("x: " )))

for i in range(len(x)):
	x[i] = 2*x[i]
	
print(x)