from numpy import *
vec=array(eval(input()))
a=0
b=0
while a<size(vec):
	b+=vec[a]*(a+1)
	a+=1
print(b)