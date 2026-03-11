nasc= int(input(" "))
pais = input(" ")

idade = 2023 - nasc

if pais == "B" and idade < 21:
	print("nao")
	pais(21 - idade)
elif pais == "E" and idade > 21:
	print("sim")
	pais(18 - idade)
	