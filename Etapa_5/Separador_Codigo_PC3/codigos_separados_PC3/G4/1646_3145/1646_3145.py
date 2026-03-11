from numpy import *
x=array(eval(input()))
a=0
b=0
c=0
for q in x:
	if q<=50:
		a+=1
s=ones(a, dtype=int)
for q in x:
	if q<=50:
		s[b]=c
		b+=1
	c+=1
print(a)
print(s)