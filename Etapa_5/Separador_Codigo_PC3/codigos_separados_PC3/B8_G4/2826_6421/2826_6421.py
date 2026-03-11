from  numpy import *
x = array(eval(input(" : ")))
i = 0
while i < size(x):
	if x[i] <= 2:
		x[i] = 0
	elif (x[i] >= 8):
		x[i] = 10
	i= i + 1	
print(x)	