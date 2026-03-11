from numpy import*
vetor = array(eval(input(":")))

cont=0
ponto=0

while(cont<size(vetor)):
	if(vetor[cont]== 1):
		ponto = ponto + 10
	elif(vetor[cont]== 2):
		ponto = ponto + 5
	elif(vetor[cont]== 3):
		ponto = ponto + 0
	elif(vetor[cont]== 4):
		ponto = ponto + 5
	elif(vetor[cont]== 5):
		ponto = ponto + 20
	elif(vetor[cont]== 6):
		ponto = ponto + 10
	cont+=1

print(sum(ponto))