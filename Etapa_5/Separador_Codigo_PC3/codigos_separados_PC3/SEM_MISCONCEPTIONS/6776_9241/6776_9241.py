ano= int(input("digite o seu ano de nascimento: "))
pais= input("digite (B) para Brasil ou (R) para Reino Unido: "). upper()

idade= 2023 - ano
if pais == "B":
	if idade >= 18:
		print("sim")
		idade= (2023 - ano) - 18
		print(idade)
	else:
		print("nao")
		idade= 18- (2023 - ano)
		print(idade)
elif pais == "R":
	if idade >= 17:
		print("sim")
		idade= (2023- ano) - 17
		print(idade)
	else:
		print("nao")
		idade= 17 - (2023 - ano)
		print(idade)
else:
 print("invalido")