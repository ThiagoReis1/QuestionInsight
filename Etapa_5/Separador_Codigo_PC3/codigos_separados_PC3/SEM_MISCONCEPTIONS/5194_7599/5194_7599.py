clas = input("classificao da missao:").upper()
valor = float(input("valor:"))
if(clas=="B"):
	print("Classe: Chunin")
	print(round (valor - (valor*(15/100)),2))
else:
	print("Classe: Jounin")
	print(round(valor - (valor*(22/100)),2))