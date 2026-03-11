C = input("Continente: ")
P = input("País: ")

if C == "America-do-Sul" and P == "Brasil":
	R = "CRISTO REDENTOR"
	print(R.upper())
elif C == "America-do-Sul" and P == "Peru":
	R = "MACHU PICCHU"
	print(R.upper())
elif C == "Asia" and P == "India":
	R = "TAJ MAHAL"
	print(R.upper())
elif C == "Asia" and P == "Jordania":
	R = "AS RUINAS DE PETRA"
	print(R.upper())
else:
	print("INFORMACAO NAO IDENTIFICADA")

	