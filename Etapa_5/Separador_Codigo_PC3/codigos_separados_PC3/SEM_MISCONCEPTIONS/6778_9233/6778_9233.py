ano = int(input("digite um ano: "))
pais = input("B/J: ").upper()

idade = 2023 - ano
if pais == "J":
	if idade >= 20:
		print("sim")
		idade = (2023 - ano)-20
		print(idade)
	else:
		print("nao")
		idade = 20 - (2023 - ano)
		print(idade)
elif pais == "B":
	if idade >= 21:
		print("sim")
		idade = (2023 - ano) - 21
		print(idade)
	else:
		print("nao")
		idade = 21 - (2023 - ano)
		print(idade)
else:
 print("invalido")