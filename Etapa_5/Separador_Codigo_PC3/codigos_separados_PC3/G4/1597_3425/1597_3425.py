from numpy import *

a = array(eval(input()))

i = 0

while i < size(a):
	if a[i] > 80:
		a[i] = a[i] - 5
	i = i + 1	
	
b = sum(a)	
print(round(b, 2))