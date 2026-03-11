from numpy import *
v=array(eval(input()))
p=0
for i in v:
	if v[p]== 0:
		v[p]=0
	else:
		v[p]=v[p]*2
	p+=1
print(v)