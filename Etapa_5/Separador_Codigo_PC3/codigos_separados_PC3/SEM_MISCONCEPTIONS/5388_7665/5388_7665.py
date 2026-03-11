from numpy import*

vetor = input().upper()
i=0
tamanho = len(vetor)
tot=0

while i < tamanho :
	if(vetor[i]=="A" or vetor[i]=="E" or vetor[i]=="I" or vetor[i]=="O" or vetor[i]=="U"):
		tot=tot+25.12
	else:
		tot=tot+40.18
	i=i+1
print(round(tot,2))