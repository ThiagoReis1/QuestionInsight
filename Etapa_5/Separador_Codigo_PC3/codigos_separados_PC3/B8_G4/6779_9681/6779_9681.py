ano = int(input("Qual o ano de seu nascimento: "))
pais = str(input("Qual o pais: [B] para Brasil e [J] para Japao: ")).upper ()
b = 2023 - ano
j = 2023 - ano
if pais == "B":
	if b >= 18:
		total = b -18
		print("sim")
		print(total)
	elif b <= 18:
		total = 18 - b
		print("nao")
		print(total)
elif pais == "J":
	if j >= 16:
		total = j - 16
		print("sim")
		print(total)
	elif j <= 16:
		total = 16 - j
		print("nao")
		print(total)
else:
	print("invalido")