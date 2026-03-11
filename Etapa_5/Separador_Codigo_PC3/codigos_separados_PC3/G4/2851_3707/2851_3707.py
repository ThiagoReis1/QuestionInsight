from numpy import *
a = array(eval(input()))
k = 0
for i in range(size(a)):
	if(a[i] == 99):
		k = k*2
		k = k - 99
	k = k + a[i]
	
print(k)