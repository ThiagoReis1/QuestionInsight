from numpy import*
vet = array(eval(input("digite um vetor: ")))
tam = size(vet)
cont = 0
n = tam
mul = 1
while cont< tam :
	med = vet[cont]
	mul = mul *med
	cont = cont + 1
z = mul ** (1/tam)
print(round(z, 2))
	