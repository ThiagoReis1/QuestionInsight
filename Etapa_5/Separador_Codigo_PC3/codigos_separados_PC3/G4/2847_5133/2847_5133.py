from numpy import * 

a = array(eval(input()))

for i in range(size(a)):
	a[i] = a[i] * a[i]
print(a)