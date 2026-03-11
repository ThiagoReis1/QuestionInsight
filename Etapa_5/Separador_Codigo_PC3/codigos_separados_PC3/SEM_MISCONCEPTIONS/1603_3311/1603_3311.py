from numpy import*
vetor = array(eval(input("Digite:")))
cont = 0
soma = 0
saida = 0
while(cont<size(vetor) and saida!=4):
	if(vetor[cont]==1):
		soma=soma+80
	elif(vetor[cont]==2):
		soma = soma + 40
	elif(vetor[cont]==3):
		soma = soma + 20
	else:
		saida = 4
	cont = cont + 1
print(soma)
