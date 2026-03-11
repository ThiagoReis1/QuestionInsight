from numpy import *
string = input()
cont = zeros(6,int)
vet = string.split(',')
for x in range(size(vet)):
	if(vet[x]=="MC"):
			cont[0] = cont[0] + 1
	elif(vet[x]=="C"):
			cont[1] = cont[1] + 1
	elif(vet[x]=="CM"):
			cont[2] = cont[2] + 1
	elif(vet[x]=="EM"):
			cont[3] = cont[3] + 1
	elif(vet[x]=="E"):
			cont[4] = cont[4] + 1
	elif(vet[x]=="ME"):
			cont[5] = cont[5] + 1
print(max(cont))
print(cont)
			
	
