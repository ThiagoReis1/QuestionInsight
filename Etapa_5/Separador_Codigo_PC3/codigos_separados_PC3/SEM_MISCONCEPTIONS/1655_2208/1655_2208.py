from numpy import*

entrada=input("Digite a estrada: ")

vetor=entrada.split(',')
estados=["AC","AM","PA","RO","RR"]

saida=zeros(size(estados),dtype=int)

for i in range (size(estados)):
	for j in range(size(vetor)):
		if(vetor[j] == estados[i]):
			saida[i]=saida[i]+1

print(max(saida))
print(saida)


	
	
print(vetor)