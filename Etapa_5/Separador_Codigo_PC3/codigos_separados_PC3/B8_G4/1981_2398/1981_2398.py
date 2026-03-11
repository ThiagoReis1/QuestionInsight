rt = input("Campeao ou Vice-Campeao? ")
vr = input("n-vezes: ")

if (rt == "Campeao"):
	if(vr=="06-vezes"):
		print("CORINTHIANS")
	elif (vr=="03-vezes"):
		print("SANTOS")
	else:
		print("TIME DE FUTEBOL NAO IDENTIFICADO")
elif (rt == "Vice-Campeao"):
	if (vr == "01-vez"):
		print("FLAMENGO")
	elif (vr == "06-vezes"):
		print("INTERNACIONAL")
	else:
		print("TIME DE FUTEBOL NAO IDENTIFICADO")