from numpy import*
v=array(eval(input('v:')))
A=min(v)
B=max(v)
C=0.75*A+0.25*B
D=0.25*A+0.75*B
x=array([0,0])
x1=0
x2=0
for i in v:
	if A<=i<C:
		x1=x1+1
		
	if D<=i<B:
		x2=x2+1
x[0]=x1
x[1]=x2
print(x)
	