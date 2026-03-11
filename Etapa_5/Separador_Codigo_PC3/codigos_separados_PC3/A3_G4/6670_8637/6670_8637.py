from numpy import *
v=array(eval(input()))
n=0
soma=0
for i in range(size(v)):
	if v [i]>20:
		soma=soma+v[i]
		n+=1
if n>0:
	m=sum(v)/(v)
	soma+=1
else:
	m=0.0
	
print(round(soma,2))
	