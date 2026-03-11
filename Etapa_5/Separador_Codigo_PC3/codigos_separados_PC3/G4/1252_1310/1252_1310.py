from numpy import *
v=array(eval(input("v: ")))
B=max(v)
A=min(v)
C=((0.6*A)+(0.4*B))
D=((0.3*A)+(0.7*B))
g=0
e=0
z=array(zeros(2, dtype=int))
for t in v:
	if (t>A and t<C) or (t==A and t<C):
		e=e+1
	if (t>C and t<D) or (t==C and t<D):
		g=g+1
z[0]=e
z[1]=g
print(z)