entrada = input()
cont = 0
while entrada != "S":
	if entrada.upper() == "PRETA":
		cont +=1
	entrada = input()
print(cont)