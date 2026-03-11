nasc = int(input("Digite o ano: "))
pais = input("B/E: ").upper()

idade = 2023 - nasc
if pais == "E":
	if idade >= 18:
		print("sim")
		idade = (2023 - nasc) - 18
		print(idade)
	else:
		print("nao")
		idade = 18 - (2023 - nasc)
		print(idade)
elif pais == "B":
	if idade >= 21:
		print("sim")
		idade = (2023 - nasc) - 21
		print(idade)
	else:
		print("nao")
		idade = 21 - (2023 - nasc)
		print(idade)
else:
	print ("invalido")