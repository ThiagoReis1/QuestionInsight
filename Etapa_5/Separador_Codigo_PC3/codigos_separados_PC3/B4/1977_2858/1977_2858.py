from math import*
genero = input("Digite o genero da serie: ")
sub_g = input("Digite o subgenero da serie: ")

if(((genero.upper() != "INVESTIGATIVA") and (genero.upper() != "DRAMATICA")) or ((sub_g.upper() != "SUSPENSE") and (sub_g.upper() != "DRAMA") and (sub_g.upper() != "COM FICCAO") and (sub_g.upper() != "AVENTURA"))):
	print("SERIE NAO IDENTIFICADA")
elif((genero.upper() == "INVESTIGATIVA") and (sub_g.upper() == "SUSPENSE")):
	print("DEXTER")
elif((genero.upper() == "INVESTIGATIVA") and (sub_g.upper() == "DRAMA")):
	print("NARCOS")
elif((genero.upper() == "DRAMATICA") and (sub_g.upper() == "COM FICCAO")):
	print("LOST")
elif((genero.upper() == "DRAMATICA") and (sub_g.upper() == "AVENTURA")):
	print("SHERLOCK")
else:
	print("SERIE NAO IDENTIFICADA")