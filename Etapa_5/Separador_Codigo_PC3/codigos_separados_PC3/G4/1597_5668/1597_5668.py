from numpy import *
p = array(eval(input("produtos: ")), dtype = float)
for i in range(size(p)):
	if p[i] > 80.0:
		p[i] = p[i] - 5
v = sum(p)
print(round(v, 2))