import numpy as np
vet = np.array(eval(input()))
z = x = 0
for i in vet:
	if i >= 2000:
		z = z+ 1
saida = np.zeros(z, dtype=int)
for p in range(0,len(vet),1):
	if vet[p] >= 2000:
		saida[x] = p
		x = x+1
print(z)
print(saida)
	