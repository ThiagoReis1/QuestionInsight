casas = input()

preta = 0

while(casas.upper() != "S"):
	if (casas.upper() == "PRETA"):
		preta = preta + 1

	casas = input()
print(preta)