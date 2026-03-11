vet = input("cor da pele: ").upper().split(',')

cont = [0,0,0,0,0,0]

for i in vet:
	if i == "MC":
		cont[0] = cont[0] + 1
		
	elif i == "C":
		cont[1] = cont[1] + 1
		
	elif i == "CM":
		cont[2] = cont[2] = 1
		
	elif i == "EM":
		cont[3] = cont[3] + 1
		
	elif i == "E":
		cont[4] = cont[4] + 1
		
	elif i == "ME":
		cont[5] = cont[5] + 1
		
maximo = max(cont)

print(maximo)

print(cont)