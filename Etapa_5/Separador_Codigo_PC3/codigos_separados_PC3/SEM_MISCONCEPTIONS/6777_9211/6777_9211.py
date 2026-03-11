ano = int(input("ano do nascimento"))
pais = input("pais (B/I):").upper()
if pais == "B":
	idade = 2023 - ano
	if idade <  18 :
		print("nao")
		print((ano + 18) - 2023)
	else:
		print("sim")
		print(2023 - (ano + 18))
elif pais == "I" :
	idade = 2023 - ano
	if idade < 17 :
			print("nao")
			print((ano + 17) - 2023 )
	else :
		print("sim")
		print(2023 - (ano + 17))
else:
	print(invalido)