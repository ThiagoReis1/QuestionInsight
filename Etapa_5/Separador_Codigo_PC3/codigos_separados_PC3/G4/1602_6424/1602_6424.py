from numpy import *
x = array(eval(input()))
i = 0
while x[i] != max(x):
	i += 1
print(i)	