from numpy import * 

v = input("Digite os itens: ").upper().split(',')
cont = zeros(4, dtype=int)

for x in v:
	if (x == "A"):
		cont[0] = cont[0] + 1
	elif (x == "B"):
		cont[1] = cont[1] + 1
	elif (x == "L"):
		cont[2] = cont[2] + 1
	elif (x == "H"):
		cont[3] = cont[3] + 1
		
print(cont)