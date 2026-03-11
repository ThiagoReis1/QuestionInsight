cor = input("Informe a cor da casa da roleta: ").upper()
acum = 0

while cor != "S":
	if cor == "PRETA":
		acum = acum+1
	cor = input("Informe a cor da casa da roleta: ").upper()

print(acum)