from numpy import *

a = array(eval(input()))

for i in range (size(a)):
	if a [i] == 9:
		a [i]=0
	else:
		a[i]+= 1
print(a)