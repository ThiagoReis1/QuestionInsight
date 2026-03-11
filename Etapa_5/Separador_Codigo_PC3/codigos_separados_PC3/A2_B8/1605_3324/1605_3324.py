from numpy import*
vetor= array(eval(input()))
i=0
soma=200
while(i<size(vetor)):
	if(vetor[i]==1):
		soma= soma*4
	elif(vetor[i]==2):
		soma= soma*2
	elif(vetor[i]==3):
		soma= soma
	elif(vetor[i]==4):
		soma= soma/2
	i= i + 1
print(round(soma,2))
