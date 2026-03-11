from numpy import*
v = array(eval(input()))
x = array([0,0])
B = v[0]
A = min(v)
B = max(v)
C = 0.7*A + 0.3*B
D = 0.4*A + 0.6*B
x1 = 0
x2 = 0
for i in range(size(v)):
	if(v[i]>=A and v[i]<C):
		x1 = x1+1
	elif(v[i]>=C and v[i]<D):
		x2 = x2 + 1
x[0] = x1
x[1] = x2
print(x)