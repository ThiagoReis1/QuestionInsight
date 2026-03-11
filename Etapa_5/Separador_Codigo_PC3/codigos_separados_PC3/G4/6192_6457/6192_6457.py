cor = input("Digite a cor da casa: ").upper()

cont = 0

while cor != "S":
	if cor == "PRETA":
		cont = cont + 1
	cor = input("Digite a cor da casa: ").upper()
print(cont)