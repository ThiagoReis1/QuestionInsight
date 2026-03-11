from numpy import*
vet1 = array(eval(input("notas dos alunos ")))
reprov = 0
for i in range(size(vet1)):
	if(vet1[i] < 5):
		reprov = reprov + 1
cont = zeros(reprov, dtype=int)
k = 0
for j in range(size(vet1)):
	if(vet1[j] < 5):
		cont[k] = cont[k] + j
		k = k + 1
print(reprov)
print(cont)