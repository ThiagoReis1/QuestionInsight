ano_nasc = int(input("ano nascimento"))
pais = input("B ou E")
pais = pais.upper()

idade = 2023 - ano_nasc

if (pais =="E"):
	if idade >=18:
		print("sim")
		print(idade-18)
	else:
		print("não")
		print(18-idade)
elif (pais=="B"):
	if idade >=21:
		print("sim")
		print(idade-21)
	else:
		print("nao")
		print(21-idade)
else:
	print("invalido")