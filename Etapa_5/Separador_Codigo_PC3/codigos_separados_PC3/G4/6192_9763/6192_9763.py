casa = input("Informe a cor da casa: ").upper()
cont = 0

while (casa != "S"):
	if casa == "PRETA":
		cont = cont + 1
	casa = input("Informe a cor da casa: ").upper()
	
print(cont)