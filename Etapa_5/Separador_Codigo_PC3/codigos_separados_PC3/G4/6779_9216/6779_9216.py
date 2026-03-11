ano = int(input ("Digite o ano de nascimento: "))
pais = input ("Digite B para Brasil e J para Japao: ")

idade = 2023 - ano

if (pais.upper() == "B"):
	if (idade >= 18):
		x = idade - 18
		print ("sim")
		print (x)
	else:
		x = 18 - idade
		print ("nao")
		print (x)
elif (pais.upper() == "J"):
	if (idade >= 16):
		x = idade - 16
		print ("sim")
		print (x)
	else:
		x = 16 - idade
		print ("nao")
		print (x)
else:
	print ("invalido")