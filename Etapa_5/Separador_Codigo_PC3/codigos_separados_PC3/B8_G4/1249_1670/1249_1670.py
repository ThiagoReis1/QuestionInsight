from numpy import *
v=array(eval(input()))
v1=array(zeros(2, dtype=int))
A=min(v)
B=max(v)
C = 0.7*A + 0.3*B
D = 0.4*A + 0.6*B

for i in range (size(v)):
	if v[1]>=A and v[i]<C:
		v1[0]=v1[0]+1
	elif v[i]>=C and v[i]<D:
		v1[1]=v1[1]+1
print(v1)
