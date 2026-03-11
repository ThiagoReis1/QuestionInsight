from numpy import*
vetor = array(eval(input("Digite:")))
cont = 0
while(cont<size(vetor)):
	if(vetor[cont]==min(vetor)):
		i = cont
	cont=cont+1
print(i)