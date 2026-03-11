import numpy as np
x = np.array(eval(input()))
k = len(x)
cont = p = soma = 0
peso = 1
while p < k:
	cont = x[p]*peso
	soma = soma + cont
	p = p+ 1
	peso = peso + 1
print (soma)