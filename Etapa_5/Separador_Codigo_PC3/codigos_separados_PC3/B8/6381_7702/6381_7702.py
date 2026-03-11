from numpy import*
naipe = input("naipe: ").upper().split(",")
cont = zeros(4, dtype=int)

for x in naipe:
	if x == "C":
		cont[0] = cont[0] + 1
	elif x == "O":
		cont[1] = cont[1] + 1
	elif x == "P":
		cont[2] = cont[2] + 1
	elif x == "E":
		cont[3] = cont[3] + 1
print(cont)
		