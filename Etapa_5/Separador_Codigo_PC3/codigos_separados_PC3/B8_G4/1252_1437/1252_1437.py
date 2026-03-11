from numpy import *

v = array(eval(input()))
a = min(v)
b = max(v)
c = 0.6*a + 0.4*b
d = 0.3*a + 0.7*b

x1 = 0 
x2 = 0

for i in v:
	if (i >= a) and (i < c):
		x1 = x1 + 1
	elif (i >= c) and (i < d):
		x2 = x2 + 1
x = array([x1,x2])
print(x)
		
