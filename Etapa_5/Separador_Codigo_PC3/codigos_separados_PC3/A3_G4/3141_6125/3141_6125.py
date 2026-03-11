from numpy import *
v= array(eval(input()))
p= 0
m= 0
for i in range(size(v)):
	m= m + v[i]**(1/6)
m = (m/size(v))**6
print(round(m, 2))		