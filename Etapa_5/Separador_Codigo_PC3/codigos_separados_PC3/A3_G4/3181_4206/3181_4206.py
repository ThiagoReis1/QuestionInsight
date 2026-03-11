from numpy import *
a = array(eval(input()))
b = array(zeros(37,dtype = int))
t = 0
for i in range(0,size(a)):
	b[a[i]] = b[a[i]]+1
	
print(b)