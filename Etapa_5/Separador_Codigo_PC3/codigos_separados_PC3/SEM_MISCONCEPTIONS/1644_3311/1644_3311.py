from numpy import*
vetor = array(eval(input("Digite o vetor:")))
reprovados=0
aprovados = 0
for cont in vetor:
	if(cont <5):
		reprovados = reprovados+1
	else:
		aprovados=aprovados+1
vetor_reprovados = zeros(reprovados,dtype=int)
i=0
for cont in range(0,size(vetor)):
	if(vetor[cont]):
		vetor_reprovados[i]=cont
		i=i+1
print(reprovados)
print(vetor_reprovados)