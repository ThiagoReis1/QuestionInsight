from numpy import*
vetor=array(eval(int(input("Digite as faces: ")))).split(",")
pontos=100
for i in range(vetor):
	if vetor[i]==1:
		pontos=pontos
	elif vetor[i]==2:
		pontos=pontos*2
	elif vetor[i]==3:
		pontos=pontos/3
	elif vetor[i]==4:
		pontos=pontos*4
	elif vetor[i]==5:
		pontos=pontos*5
	elif vetor[i]==6:
		pontos=pontos*6
print(round(pontos,2))