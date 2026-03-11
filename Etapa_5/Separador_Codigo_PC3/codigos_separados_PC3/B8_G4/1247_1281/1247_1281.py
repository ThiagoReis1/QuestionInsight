from numpy import *
v=array(eval(input("vetor")))
A=min(v)
B=max(v)
C=0.75*A + 0.25*B
D=0.25*A + 0.75*B
k=0
l=0
for i in v:
	if i >= A and i < C:
		k=k+1
	elif i >=D and i < B:
		l=l+1
x=array([k, l])
print(x)
	