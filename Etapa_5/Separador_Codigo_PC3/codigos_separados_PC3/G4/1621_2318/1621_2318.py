from numpy import*
vet = array(eval(input()))
vet2 = array(eval(input()))

i = 0 
conta = 0

while(i < size(vet2)):
	if(vet[i] == "ARROZ"):
		conta = conta + (1.25*vet2[1])
	elif(vet[i] == "FEIJAO"):
		conta = conta + (2.60*vet2[i])
	elif(vet[i] == "BIS"):
		conta = conta + (1.80*vet2[i])
	elif(vet[i] == "MIOJO"):
		conta = conta+ (0.85*vet2[i])
	else:
		conta = conta + (3.20*vet2[i])
		
	i = i + 1
print(round(conta,2))