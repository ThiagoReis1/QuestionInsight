num = int(input("Qual o ano de nascimento?"))
pais = input("qual o pais? B ou J?")

idade = 2023 - num

if pais.upper() == "B":
	if idade >= 18:
		print("sim")
		print(idade-18)
	else:
		print("nao")
		print(18-idade)
elif pais.upper() == "J":
	if idade >= 16:
		print("sim")
		print(idade-16)
	else:
		print("nao")
		print(16-idade)
else:
	print("invalido")

			