from numpy import*
from numpy.linalg import*
v = array(eval(input(": ")))

x = shape(v)[0]
a = zeros(x, dtype= float)
for i in range(x):
	a[i] = min(v[i,:])
	
t=0
u = min(a)
for i in range(size(a)):
	if( a[i] == u):
		t = a[i]
print(t) 
