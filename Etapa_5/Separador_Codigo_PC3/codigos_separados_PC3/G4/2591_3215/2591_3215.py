from numpy import *
v=array(eval(input("")))
q=0
b=v[0]
for i in range(size(v)):
	if v[i]<0:
		y=v[i]*-1
		if y>=(b):
			print(i)
			q=q+1
print(q)