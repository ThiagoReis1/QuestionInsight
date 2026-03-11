from numpy import*
cont = zeros(4, dtype=int)
vet = array(eval(input("TIME: ")))
for i in range(size(vet)):
	if (vet[i] == 'BOTAFOGO'):
		cont[0] = cont[0] + 1
	elif(vet[i] == 'FLAMENGO'):
		cont[1] = cont[1] + 1
	elif(vet[i] == 'FLUMINENSE'):
		cont[2] = cont[2] + 1
	elif(vet[i] == 'VASCO'):
		cont[3] = cont[3] + 1

print(cont)
			  