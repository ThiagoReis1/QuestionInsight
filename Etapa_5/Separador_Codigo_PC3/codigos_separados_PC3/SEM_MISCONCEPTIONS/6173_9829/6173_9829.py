resposta = input("O atendimento foi satisfatorio?: ").upper()

count = 0
while resposta != 'S':
	resposta = input("O atendimento foi satisfatorio?: ").upper()
	if resposta == "SIM":
		count += 1
print(count)