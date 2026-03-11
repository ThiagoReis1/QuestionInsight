from numpy import*

vet1 = array(eval(input("produtos")))
vet2 = array(eval(input("quantidade ")))

i = 0
soma = 0

while(i < size(vet1)):
	if(vet1[i]== "ARROZ"):
		soma = soma + 1.25 * vet2[i]
	elif(vet1[i]=="FEIJAO"):
		soma = soma + 2.60 * vet2[i]
	elif(vet1[i]=="BIS"):
		soma = soma + 1.80 * vet2[i]
	elif(vet1[i]=="MIOJO"):
		soma = soma + 0.85 * vet2[i]
	elif(vet1[i]=="FANTA"):
		soma = soma + 3.20 * vet2[i]
	i = i + 1
print(soma)
