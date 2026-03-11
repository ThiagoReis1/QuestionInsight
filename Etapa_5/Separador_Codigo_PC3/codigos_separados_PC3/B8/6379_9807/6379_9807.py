from numpy import * 

notas = (input('insira: ')).upper().split(",")
cont = zeros(5, dtype=int)

for i in notas:
	if i == 'A':
		cont[0] += 1
	elif i == 'B':
		cont[1] += 1
	elif i == 'C':
		cont[2] += 1
	elif i == "D":
		cont[3] += 1
	elif i == 'E':
		cont[4] += 1

print(cont)
