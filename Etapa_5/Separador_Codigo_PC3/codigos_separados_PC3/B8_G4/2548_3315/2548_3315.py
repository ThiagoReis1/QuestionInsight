from numpy import*

nome = input()

var = ""
i=0
while(i<len(nome)):
	if(i==0):
		var = var + nome[i]
	elif(nome[i]==" "):
		var = var + nome[i+1]
	i=i+1

print(var.upper())	