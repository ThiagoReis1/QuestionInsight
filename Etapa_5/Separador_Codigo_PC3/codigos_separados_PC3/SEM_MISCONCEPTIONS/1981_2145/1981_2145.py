time = input("Digite o resultado do time nessa competicao: (Campeao/Vice-campeao): ")
vezes = input("Vezes que o time alcancou o resultado: (06-vezes/03-vezes/01-vez)")

if (time.upper() == "CAMPEAO") and (vezes == "06-vezes"):
	print("CORINTHIANS")
elif(time.upper() == "CAMPEAO") and (vezes == "03-vezes"):
	print("SANTOS")
elif(time.upper() == "VICE-CAMPEAO") and (vezes == "01-vez"):
	print("FLAMENGO")
elif(time.upper() == "VICE-CAMPEAO") and (vezes == "06-vez"):
	print("INTERNACIONAL")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")