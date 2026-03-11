from numpy import*

nome= input('nome:').upper()
custo=0
i=0
v=0
while(i<len(nome)):
	if(nome[i]=='A'):
		v=v+1
	elif(nome[i]=='E'):
		v=v+1
	elif(nome[i]=='I'):
		v=v+1
	elif(nome[i]=='O'):
		v=v+1
	elif(nome[i]=='U'):
		v=v+1
	i=i+1
cv= v*0.12
cc= (len(nome)-v)*0.18

print(round(cc+cv,2))

	