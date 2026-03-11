from numpy import*
vet1 = array(eval(input("notas dos alunos ")))
vet2 = array(eval(input("notas dos alunos ")))
cont = zeros(size(vet1), dtype=float)
a = 0
for i in range(size(vet1)):
	cont[i] = cont[i] + vet1[i]
for j in range(size(vet2)):
	cont[j] = cont[j] + vet2[j]
for k in range(size(cont)):
	if(cont[k] >= 12):
		a = a + 1
print(cont)
print(a)
	