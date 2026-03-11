from numpy import*
vet = input("").split(',')
cont = zeros(5, dtype=int)

for i in vet:
	if i == "P":
		cont[0] = cont[0] + 1
	elif i == "C":
		cont[1] = cont[1] + 1
	elif i == "M":
		cont[2] = cont[2] + 1
	elif i == "V":
		cont[3] = cont[3] + 1
	elif i == "A":
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)