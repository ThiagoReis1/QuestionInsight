from numpy import *

v = array(eval(input("Digite o valor do intem: ")))

b = 0

for i in range(size(v)):
	if(v[i] > 160):
		v[i] = v[i] - 25
	b = sum(v)
print(round(b, 2))