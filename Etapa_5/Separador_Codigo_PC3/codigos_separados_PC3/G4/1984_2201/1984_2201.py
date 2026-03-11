R= input().upper()
V = input().upper()

if((R == "CAMPEAO") and (V == "11-VEZES")):
	print("REAL MADRID")
elif((R == "CAMPEAO") and (V == "05-VEZES")):
	print("BARCELONA")
elif((R == "VICE-CAMPEAO") and (V == "01-VEZ")):
	print("CHELSEA")
elif((R == "VICE-CAMPEAO") and (V == "04-VEZES")):
	print("MILAN")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")

