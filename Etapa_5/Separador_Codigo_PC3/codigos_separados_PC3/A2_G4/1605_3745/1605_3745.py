from numpy import*
vet = array(eval(input("Digite o vetor: ")))
p = 200
i = 0
while(i < size(vet)):
	if(vet[i] == 1):
		p = p * 4
	if(vet[i] == 2):
		p = p * 2
	if(vet[i] == 3):
		p = p
	if(vet[i] == 4):
		p = p/2
	i = i + 1
print(round(p,2))


