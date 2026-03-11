from numpy import*
n=input("senha: ").upper()
i=0
cont=0
while(i<len(n)):
	if(n[i]=="A" or n[i]=="E" or n[i]=="I" or n[i]=="O" or n[i]=="U"):
		cont=cont+1.12
	else:
		cont=cont+1.18
	i=i+1
print(round(cont,2))