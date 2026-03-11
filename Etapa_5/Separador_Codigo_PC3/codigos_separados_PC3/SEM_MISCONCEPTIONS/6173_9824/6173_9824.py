resposta = input('digite a resposta: ').upper()

cont = 0

while resposta != "S":
	if resposta == "SIM":
		cont += 1
	resposta = input('digite a resposta: ').upper()

print(cont)
	