from numpy import*

vet=input()

x=len(vet)
i=0

tot=0

while(i<x):
	if(vet[i]=="A" or vet [i] == "E" or vet[i] == "I" or vet[i]=="O" or vet[i] == "U"):
		tot=tot+45.12
	else:
		tot=tot+50.18
	i=i+1

print(round(tot,2))