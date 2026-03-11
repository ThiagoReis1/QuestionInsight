from numpy import*
#cria o vetor de 5 categorias com 0
cont = zeros(5, dtype=int)

#leitura do vetor 
vet = input(": ").upper().split(',')

#contagem de ocorrencias
for i in range(size(vet)):
	if(vet[i]=='CHN'):
		cont[0] = cont[0] + 1
	elif(vet[i] =='JPN'):
		cont[1] = cont[1] + 1 
	elif(vet[i] =='KOR'):
		cont[2] = cont[2] + 1
	elif(vet[i] =='MGL'):
		cont[3] = cont[3] + 1
	elif(vet[i]=='THA'):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)