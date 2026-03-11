time_escolhido = input("resultado do tipo de futebol:")
quantidade_de_vezes_campeao = input("quantidade de vezes campeao:")

if (time_escolhido == "Campeao" or quantidade_de_vezes_campeao == "06-vezes"):
	print("CORINTHIANS".upper())
elif(time_escolhido == "Campeao" or quantidade_de_vezes_campeao == "03-vezes"):
	print("SANTOS".upper())
elif(time_escolhido == "Vice-Campeao" or quantidade_de_vezes_campeao == "01-vez"):
	print("FLAMENGO".upper())
elif(time_escolhido == "Vice-Campeao" or quantidade_de_vezes_campeao == "06-vezes"):
	print("INTERNACIONAL".upper())
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")