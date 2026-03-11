import numpy as np
x = np.array(eval(input()))
tam = len(x)
k = 0
p = 0
while p < tam:
	k = k + int(x[p])
	if k > 75:
		k = 75
	p = p+ 1
print(k)