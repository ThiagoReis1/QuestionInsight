win = input("campeao ou vice?: ").upper()
qt = input("quantas vezes?: ")

if (win == "CAMPEAO" and qt == "11-vezes"):
	print("REAL MADRID")
elif (win == "CAMPEAO" and qt == "05-vezes"):
	print("BARCELONA")
elif (win == "VICE-CAMPEAO" and qt == "01-vez"):
	print("CHELSEA")
elif (win == "VICE-CAMPEAO" and qt == "04-vezes"):
	print ("MILAN")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")