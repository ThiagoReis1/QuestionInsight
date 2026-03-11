from numpy import*
vet = array(eval(input("Frequencia: ")))

alunos = 0

for e in range(size(vet)):
	if(vet[e] >= 70):
		alunos = alunos + 1

vet2 = zeros(alunos, dtype=int)

j = 0
for e in range(size(vet)):
	if(vet[e] >= 70):
		vet2[j] = e
		j = j + 1
		
print(alunos)
print(vet2)

