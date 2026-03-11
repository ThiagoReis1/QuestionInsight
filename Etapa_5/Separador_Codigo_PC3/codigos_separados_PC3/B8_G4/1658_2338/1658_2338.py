from numpy import*
cont = zeros(5,dtype = int)
vet = input("digite: ").upper().split(',')


for i in range(size(vet)):
	if(vet[i] == "CHN"):
		cont[0] = cont[0]+1
		
	elif(vet[i] == "JPN"):
		cont[1] = cont[1]+1

	elif(vet[i] == "KOR"):
		cont[2] = cont[2]+1
		
	elif(vet[i] == "MGL"):
		cont[3] = cont[3]+1

	elif(vet[i] == "THA"):
		cont[4] = cont[4]+1

print(max(cont))
print(cont)