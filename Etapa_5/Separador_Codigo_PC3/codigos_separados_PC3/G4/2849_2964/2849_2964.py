import numpy as np

v = np.array(eval(input()))
soma = 0

for i in range(0, v.size):
	soma += v[i]	
	if(v[i] == 0):
		soma = 0

print(soma)