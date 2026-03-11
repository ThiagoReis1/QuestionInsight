from numpy import *
p = array(eval(input("")))
q = array(eval(input("")))

x = 0

for i in range(size(p) == size(q)):

	d = x + (p[i] - q[i])**2

d = sqrt(d)	
s = 1/(1+d)
print(round(d, 4))
print(round(d, 2))
		
		