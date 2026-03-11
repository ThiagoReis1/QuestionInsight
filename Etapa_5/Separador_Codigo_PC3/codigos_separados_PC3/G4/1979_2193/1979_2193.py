S = input("").upper()
V = input("").upper()
if ((S == "CAMPEAO") and (V == "05-VEZES")):
	print("BRASIL")
elif ((S == "CAMPEAO") and (V == "04-VEZES")):
	print("ITALIA")
elif ((S == "VICE-CAMPEAO") and (V == "04-VEZES")):
	print("ALEMANHA")
elif ((S == "VICE-CAMPEAO") and (V == "03-VEZES")):
	print("ARGENTINA")
else:
	print("SELECAO NAO IDENTIFICADA")