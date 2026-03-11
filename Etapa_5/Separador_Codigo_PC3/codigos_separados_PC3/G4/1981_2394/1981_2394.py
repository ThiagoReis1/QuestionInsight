x = input()
qtd = input()
if(x == "Campeao" and qtd == "06-vezes"):
	print("corinthians".upper())
elif(x == "Campeao" and qtd == "03-vezes"):
	print("santos".upper())
elif(x == "Vice-Campeao" and qtd == "01-vez"):
	print("flamengo".upper())
elif(x == "Vice-Campeao" and qtd == "06-vezes"):
	print("internacional".upper())
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO".upper())