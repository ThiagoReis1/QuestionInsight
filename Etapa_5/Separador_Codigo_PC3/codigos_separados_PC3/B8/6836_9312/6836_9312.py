from numpy import*
vetor = input("")
acum = 0
i = 0
while(i<len(vetor)):
	if(vetor[i] == "B"):
		acum = acum + 6.8
	elif(vetor[i] == "C"):
		acum = acum + 11.75
	elif(vetor[i] == "M"):
		acum = acum + 5.90
	i = i + 1
print(round(acum,2))
