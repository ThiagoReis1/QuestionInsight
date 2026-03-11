from numpy import *
minimo = 0
maximo = 40
v = array(eval(input("Infome o vetor: ")))
i = 0
q = 0
while(i < size(v)):
	if((minimo <= v[i]) and (v[i] <= maximo)):
		q = q + 1
	i = i + 1
v2 = ones(q, dtype = float)
i = 0
k = 0
while(i < size(v)):
	if((minimo <= v[i]) and (v[i] <= maximo)):
		v2[k] = v[i]
		k = k + 1
	i = i + 1
print(v2)