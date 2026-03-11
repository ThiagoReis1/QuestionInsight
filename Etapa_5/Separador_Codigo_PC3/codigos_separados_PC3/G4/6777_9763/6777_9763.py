ano = int(input("informe o ano de nascimento: "))
p = input("informe o pais: ").upper()
i = 2023 - ano
if p == "B":
	if i >= 18:
		print("sim")
		print(i - 18)
	else:
		print("nao")
		print(18 - i)
elif p == "I":
	if i >= 17:
		print("sim")
		print(i - 17)
	else:
		print("nao")
		print(17 - i)
else:
	print("invalido")
