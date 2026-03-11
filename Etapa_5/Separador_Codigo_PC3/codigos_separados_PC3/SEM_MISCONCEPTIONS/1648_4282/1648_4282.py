from numpy import *

rps = 0
vet = array(eval(input()))

for i in range(size(vet)):
	if (vet[i] < 70):
		rps += 1
print(rps)

entrada = 0
saida = 0
vet_idx = zeros(rps, dtype=int)
for i in vet:
	if (i < 70):
		vet_idx[saida] += entrada
		saida += 1
	entrada += 1
print(vet_idx)