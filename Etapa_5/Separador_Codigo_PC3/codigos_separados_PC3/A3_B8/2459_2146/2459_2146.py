peso = float(input("Peso do produto: "))
distancia = float(input("Distancia: "))
codigo = input("Codigo estado: ")
custokg = 25
custokm = 0.10

icms1 = 17
icms2 = 17.5
icms3 = 18
icms4 = 20

sevico1 = (peso * custokg + distancia * custokm) * (1 + (icms1 / 100))

if(codigo == 1 or codigo == 2 or codigo == 3 or codigo == 4):
	if(codigo == 1):
		print(servico1)
	elif(cidade == "Bravos"):
		print("bravosiano")
	elif(cidade == "Lys"):
		print("liseno")
	elif(cidade == "Qohor"):
		print("qohorik")