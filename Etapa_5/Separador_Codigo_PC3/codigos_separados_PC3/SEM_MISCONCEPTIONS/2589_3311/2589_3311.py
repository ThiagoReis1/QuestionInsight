from numpy import*
vetor = array(eval(input("Digite:")))
acumulador=0
for cont in range(1,size(vetor)):
	if(vetor[cont]>=vetor[0]):
		print(cont)
		acumulador=acumulador+1
print(acumulador)