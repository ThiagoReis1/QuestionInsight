time = input("resposta:").upper()
cont = 0

while (time != "X"):
	if (time == "A"):
		cont += 1
		time = input("resposta:").upper()
	else:
		cont = cont
		time = input("resposta:").upper()
print(cont)