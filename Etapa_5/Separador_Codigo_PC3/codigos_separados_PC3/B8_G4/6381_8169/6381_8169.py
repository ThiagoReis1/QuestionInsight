from numpy import*
cont = zeros(4, dtype=int)
n = (input("")).upper().split(",")
for g in range(size(n)):
	if n[g] == "C":
		cont[0] = cont[0] + 1

	elif n[g] == "O":
		cont[1] = cont[1] + 1

	elif n[g] == "P":
		cont[2] = cont[2] + 1

	elif n[g] == "E":
		cont[3] = cont[3] + 1

print(cont)