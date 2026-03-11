from numpy import*

v = array(eval(input()))
m = 1

for i in range(size(v)):
	m = m * v[i]
	p = m**(1/size(v))
print(round(p, 2))
	