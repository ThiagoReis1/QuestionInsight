from numpy import *
v = array(eval(input()))
x = array([0,0])
B = v[0]
A = min(v)
B = max(v)
C = 0.6*A + 0.4*B
D = 0.3*A + 0.7*B
x1 = 0
x2 = 0 
for i in range(size(v)):
	if(v[i]>=A and v[i]<C):
		x1 = x1 + 1
	if(v[i]>=D and v[i]<B):
		x2 = x2 + 1
x[0] = x1
x[1] = x2
print(x)



