from numpy import*

estados = input("Qual o estado: ").upper().split(",")
cont = zeros(5, dtype=int)

for i in range(0, size(estados)):
	if estados[i] == "AC":
		cont[0] += 1
	elif estados[i] == "AM":
		cont[1] += 1
	elif estados[i] == "PA":
		cont[2] += 1
	elif estados[i] == "RO":
		cont[3] += 1
	elif estados[i] == "RR":
		cont[4] += 1
print(max(cont))
print(cont)