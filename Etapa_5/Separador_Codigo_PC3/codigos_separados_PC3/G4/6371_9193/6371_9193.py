from numpy import *

v = array(eval(input("Digite os valores: ")))

v1 = zeros(size(v), dtype=int)

for i in range(size(v)):
	if v[i] == 0:
		v[i] = 9 ** 2
		v1[i] = v[i]
	else:
		v1[i] = (v[i] - 1) ** 2

print(v1)