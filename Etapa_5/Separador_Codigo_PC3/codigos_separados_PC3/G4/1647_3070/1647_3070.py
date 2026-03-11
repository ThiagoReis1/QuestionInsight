from numpy import*
vet = array(eval(input("vetor: ")))

alunapro = 0
hora = 70

for i in range(size(vet)):
	if(vet[i] >= hora):
		alunapro = alunapro + 1
print(alunapro)

nvet = zeros(alunapro, dtype=int)
p = 0

for i in range(size(vet)):
	if(vet[i] >= 70):
		nvet[p] = nvet[p] + i
		p = p + 1
print(nvet)		

		
