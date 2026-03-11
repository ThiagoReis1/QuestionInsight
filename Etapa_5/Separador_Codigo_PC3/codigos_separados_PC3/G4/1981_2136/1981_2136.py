c = input("resultado do time: ").upper()
v = input("quantas vezes o time foi campeao: ").upper()

if(c==("CAMPEAO") and v==("06-VEZES")):
	print("CORINTHIANS")
elif(c==("CAMPEAO") and v==("03-VEZES")):
	print("SANTOS")
elif(("VICE-CAMPEAO") and v==("01-VEZ")):
	print("FLAMENGO")
elif(("VICE-CAMPEAO") and v==("06-VEZES")):
	print("INTERNACIONAL")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")