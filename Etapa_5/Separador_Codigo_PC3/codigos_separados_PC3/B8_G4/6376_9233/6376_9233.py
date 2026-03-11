from numpy import*
part = input("digite a partida: ").upper()
cont = zeros(4, dtype=int)

for i in range(len(part)):
	if(part[i] == "A"):
		cont[0] += 1
	elif(part[i] == "B"):
		cont[1] += 1
	elif(part[i] == "C"):
		cont[2] += 1
	elif(part[i] == "D"):
		cont[3] += 1
print(cont)