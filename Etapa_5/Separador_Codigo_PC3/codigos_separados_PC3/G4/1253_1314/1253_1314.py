from numpy import*
v=array(eval(input("Vetor:")))

A=min(v)
B=max(v)
C=0.6*A+0.4*B
D=0.3*A+0.7*B
x=ones(2,dtype=int)
xa=0
xb=0

for i in range(size(v)):
	if	(v[i]>=A and v[i]<C):
		xa=xa+1
	if (v[i]>=D and v[i]<B):
		xb=xb+1
		
x[0]=xa
x[1]=xb
print(x)
		
	