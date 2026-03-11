from numpy import *
from math import *
v = array(eval(input()))
a = array(zeros(size(v),dtype = float))
t = 0
while(t!=size(v)):
	a[0+t]=exp(v[0+t])
	t = t+1
	
b = log(sum(a)/exp(size(v)))
print(round(b,2))

