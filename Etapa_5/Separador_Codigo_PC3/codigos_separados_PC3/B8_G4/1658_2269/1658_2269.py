from numpy import*
vet = input(": ").upper().split(',')
cont = zeros(5, dtype=int)

for I in range (size(vet)):
	if(vet[I] == "CHN"):
		cont[0] = cont[0] + 1
	elif(vet[I] == "JPN"):
		cont[1] = cont[1] + 1
	elif(vet[I] == "KOR"):
		cont[2] = cont[2] + 1
	elif(vet[I] == "MGL"):
		cont[3] = cont[3] + 1 
	elif(vet[I] == "THA"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)
		
	

 
