resposta = input("SIM OU NAO? ").upper()
i = 0 
while resposta != "S":
	if resposta == "SIM":
		i = i + 1
	resposta = input("SIM OU NAO? ").upper()
print(i)