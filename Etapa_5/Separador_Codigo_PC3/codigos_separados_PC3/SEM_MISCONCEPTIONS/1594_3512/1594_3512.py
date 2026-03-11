from numpy import*

vetor= array(eval(input("dig: ")))

dano =0
peso = 1

for i in range(0,size(vetor)):
	dano = dano + vetor [i] * peso
	peso = peso +1
	
print(dano)