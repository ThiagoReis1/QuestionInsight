from numpy import *
apr = array(eval(input("Notas dos alunos: ")))

ap = 0

for i in range(size(apr)):
	if apr[i] >= 5.0:
		ap = ap + 1

vet = zeros(ap, dtype=int)		
i = 0

for j in range(size(apr)):
	if apr[j] >= 5.0:
		vet[i] = j 
		i = i + 1
		
print(ap)
print(vet)