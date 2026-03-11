resultado = input("Opção desejada: ").upper()
n = input("numero de titulos")

if (resultado == "CAMPEAO") and (n == "06-vezes"):
	print("CORINTHIANS")
elif (n == "03-vezes"):
	print("SANTOS")
elif (resultado == "VICE-CAMPEAO") and (n == "01-vez"):
	print("FLAMENGO")
elif (n == "06-vezes"):
	print("INTERNACIONAL")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")