peso = float(input("Peso: "))
distancia = float(input("Distancia: "))
codigo = int(input("Codigo: "))

custokg = 25
custokm = 0.10
icms1 = 17
icms2 = 17.5
icms3 = 18
icms4 = 20

if ((codigo > 0) and (codigo <= 4)):
	if(codigo == 1):
		print(((peso * custokg) + (distancia * custokm)) * (1.0 + (17 / 100)))
	elif(codigo == 2):
		print(round(((peso * custokg) + (distancia * custokm)) * (1.0 + ( 17.5 / 100)),2 ))
	elif(codigo == 3):
		print(((peso * custokg) + (distancia * custokm)) * (1.0 + (18 / 100)))
	elif (codigo == 4):
		print(((peso * custokg) + (distancia * custokm)) * (1.0 + (20 / 100)))