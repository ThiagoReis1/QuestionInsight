from numpy import*

nota = input("Digite a string: ").upper().split(",")

cont = zeros(4, dtype=int)

for i in range(len(nota)):
	if nota[i] == "C":
		cont[0] += 1
	elif nota[i] == "D":
		cont[1] += 1
	elif nota[i] == "V":
		cont[2] += 1
	else:
		cont[3] += 1

print(cont)