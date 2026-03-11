from numpy import *
x=array(eval(input()))
a=0
b=0
for q in x:
	if q>=x[0] and b!=0:
		a+=1
		print(b)
	b+=1
print(a)