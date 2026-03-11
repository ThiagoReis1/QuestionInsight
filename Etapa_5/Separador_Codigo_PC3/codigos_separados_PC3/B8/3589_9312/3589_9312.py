from numpy import*
vetor = array(eval(input("")))
i = 0
acum = 0
while(i<len(vetor)):
	if(vetor[i] == 1):
		acum = acum + 80
	elif(vetor[i] == 2):
		acum = acum + 40
	elif(vetor[i] == 3):
		acum = acum + 20
	elif(vetor[i] == 4):
		acum = acum + 10
	i = i + 1
print(acum)