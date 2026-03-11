from numpy import*

vet = array(eval(input("digite um vetor: ")))
vet1 = array(eval(input("digite um vetor: ")))

i = size(vet)
j = 0
pasa = 0

while(j < i):
	pasa = pasa - vet1[j] + vet[j]
	j = j + 1
print(pasa)
