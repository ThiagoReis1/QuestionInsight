from numpy import*

trincas = array(eval(input("Tricas: ")))

cont = zeros(10, dtype=int)

for i in range(0, size(trincas), 3):
	if trincas[i] == 0:
		cont[0] += 1
	elif trincas[i] == 111:
		cont[1] += 1
	elif trincas[i] == 2:
		cont[2] += 1
	elif trincas[i] == 3:
		cont[3] += 1
	elif trincas[1] == 4:
		cont[4] += 1
	elif trincas[i] == 5:
		cont[5] += 1
	elif trincas[i] == 6:
		cont[6] += 1
	elif trincas[i] == 7:
		cont[7] += 1
	elif trincas[i] == 8:
		cont[8] += 1
	elif trincas[i] == 9:
		cont[9] += 1	
print(cont)
