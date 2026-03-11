br = 18
uk = 17
ano = int(input("ano:"))
pais = input("brasil (B) ou inglaterra (I)?").upper()
calculo = 2023 - ano

if pais == "B":
	if calculo >= 18:
		conta = 18 - calculo
		print("sim")
		print(conta)
	elif calculo < 18:
		conta = 18 - calculo
		print("nao")
		print(conta)
		
elif pais == "I":
	if calculo >= 17:
		conta = 17 - calculo
		print("sim")
		print(conta)
	elif calculo < 17:
		conta = 17 - calculo
		print("nao")
		print(conta)
else:
	print("invalido")