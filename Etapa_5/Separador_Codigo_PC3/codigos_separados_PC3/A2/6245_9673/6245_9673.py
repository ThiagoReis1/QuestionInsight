n = input("resposta: ").upper()

contadora = 0

while (n != "X"):
	if (n == "S"):
		contadora = contadora + 1
		n = input("resposta: ").upper()
	else:
		contadora = contadora
		n = input("resposta: "). upper()
print(contadora)