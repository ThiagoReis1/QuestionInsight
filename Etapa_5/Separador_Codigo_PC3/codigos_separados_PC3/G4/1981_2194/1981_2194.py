R = input("").upper()
V = input("").upper()
if ((R == "CAMPEAO") and (V == "06-VEZES")):
	print("CORINTHIANS")
elif ((R == "CAMPEAO") and (V == "03-VEZES")):
	print("SANTOS")
elif ((R == "VICE-CAMPEAO") and (V == "01-VEZ")):
	print("FLAMENGO")
elif ((R == "VICE-CAMPEAO") and (V == "06-VEZES")):
	print("INTERNACIONAL")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")