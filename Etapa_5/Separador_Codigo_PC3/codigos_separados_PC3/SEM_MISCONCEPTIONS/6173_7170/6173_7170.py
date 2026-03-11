quantidade = 0
resposta = input("SIM OU NAO?: ")

while resposta.upper() != "S":
	while resposta.upper() == "SIM":
		resposta = input("SIM OU NAO?: ")
		quantidade += 1
		
	if resposta.upper() == "NAO":
		resposta = input("SIM OU NAO?: ")

print(quantidade)