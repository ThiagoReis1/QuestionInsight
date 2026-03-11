tf = input("informe o resultado do time:").upper()
vz = input("informe a quantidade de vezes:").upper()
if (tf == "CAMPEAO" or tf == "VICE-CAMPEAO") and (vz == "06-VEZES" or vz == "03-VEZES" or vz == "01-VEZ"):
	if	((tf == "CAMPEAO") and (vz == "06-VEZES")):
		x = "CORINTHIANS"
		print(x) 
	elif ((tf == "CAMPEAO") and (vz == "03-VEZES")):
		x = "SANTOS"
		print(x) 
	elif ((tf == "VICE-CAMPEAO") and (vz == "01-VEZ")):
		x = "FLAMENGO"
		print(x) 
	elif ((tf == "VICE-CAMPEAO") and (vz == "06-VEZES")):
		x = "INTERNACIONAL"
		print(x) 
else:
	x = "TIME DE FUTEBOL NAO IDENTIFICADO"
	print(x) 
