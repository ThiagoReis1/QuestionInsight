from numpy import*
palavra=input("De a palavra: ")
n=len(palavra)
i=0
custo=0
while(i<n):
	if(palavra[i]=="A"or palavra[i]=="E"or palavra[i]=="I"or palavra[i]=="O" or palavra[i]=="U"):
		custo=custo+45.15
	else:
		custo=custo+50.17
	i=i+1
print(round(custo,2))