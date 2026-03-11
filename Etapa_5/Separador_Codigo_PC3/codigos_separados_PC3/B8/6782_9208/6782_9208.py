ano_nascimento = int(input("digite o ano de nascimento"))
pais = input("digite o pais (B/E):").lower()
idade = 2023 - ano_nascimento
if pais == "B" and pais == "E":
	if idade >=18:
		print("sim")
	else: 
		print("nao")
elif pais == "E":
	if idade >=16:
		print("sim")
	else:
		print("nao")
	