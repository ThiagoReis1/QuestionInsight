from numpy import*
pais= input("Digite o nome do pais: ")
cont= zeros(5, dtype=int)
vet= 0
for i in pais.split(','):
	if(i=="BE"):
		cont[0]= cont[0] + 1
	elif(i=="ES"):
		cont[1]= cont[1] + 1
	elif(i=="FR"):
		cont[2]= cont[2] + 1
	elif(i=="IT"):
		cont[3]= cont[3] + 1
	elif(i=="PT"):
		cont[4]= cont[4] + 1
print(max(cont))
print(cont)


	