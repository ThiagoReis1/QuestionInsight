carac1 = input("Campeao ou vice-campeoes: ")
carac2 = input("Numero de vezes: ")

if (carac1 == "Campeao") and (carac2 == "06-vezes"):
	print("Corinthians".upper())
elif (carac1 == "Campeao") and (carac2 == "03-vezes"):
	print("Santos".upper())
elif (carac1 == "Vice-Campeao") and (carac2 == "01-vez"):
	print("Flamengo".upper())
elif (carac1 == "Vice-Campeao") and (carac2 == "06-vezes"):
	print("Santos".upper())
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
									
