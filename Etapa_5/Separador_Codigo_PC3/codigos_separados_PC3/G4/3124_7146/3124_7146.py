from numpy import*
v = array(eval(input()))
x = 1

for i in range(size(v)):
	x = x * v[i]
	p = x**(1/size(v))
	
print(round(p,2))
	