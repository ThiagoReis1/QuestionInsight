from numpy import*
x = input()

cont = zeros(5, int)
vet = x.split(',')

for i in range(size(vet)):
	if(vet[i]=="CHN"):
		cont[0] = cont[0] + 1
	elif(vet[i]=="JPN"):
		cont[1] = cont[1] + 1
	elif(vet[i]=="KOR"):
		cont[2] = cont[2] + 1
	elif(vet[i]=="MGL"):
		cont[3] = cont[3] + 1
	elif(vet[i]=="THA"):
		cont[4] = cont[4] + 1
		
var = max(cont)		
print(var)
print(cont)

