from numpy import*
v = array(eval(input()))
p = 1
d = 0
m = 0
for i in range(shape(v)[0]):
	m = m + v[i]*p
	d = d + p 
	p = p + 1
m = m/d
print(round(m,2))