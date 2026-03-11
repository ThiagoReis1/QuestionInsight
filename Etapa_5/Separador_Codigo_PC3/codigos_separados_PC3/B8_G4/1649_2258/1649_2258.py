from numpy import* 
# Cria o vetor 
cont = zeros(5, dtype=int) 
# Leitura do vetor 
vet = input(": ").upper().split(',') 

for i in range(size(vet)): 
	if(vet[i] == 'P'): 
		cont[0] = cont[0] + 1 
	elif(vet[i] == 'C'): 
		cont[1] = cont[1] + 1 
	elif(vet[i] == 'M'): 
		cont[2] = cont[2] + 1 
	elif(vet[i] == 'V'):
		cont[3] = cont[3] + 1
	elif(vet[i] == 'A'):
		cont[4] = cont[4] + 1 
print(max(cont)) 
print(cont)