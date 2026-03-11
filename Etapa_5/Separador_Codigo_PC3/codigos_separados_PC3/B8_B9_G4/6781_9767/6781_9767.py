an = int ( input ("Ano de nascimento: "))
pais = str ( input ("Pais(B/E): "))

idd = 2023 - an

if pais.upper() == "B":
	if idd >= 21:
		soma = idd - 21
		print ("sim")
		print (soma)
	elif idd < 21:
		soma = 21 - idd
		print ("nao")
		print (soma)
elif pais.upper() == "E":
	if idd >= 18:
		soma = idd - 18
		print ("sim")
		print (soma)
	elif idd < 18:
		soma = 18 - idd
		print ("nao")
		print (soma)
else:
	print ("invalido")