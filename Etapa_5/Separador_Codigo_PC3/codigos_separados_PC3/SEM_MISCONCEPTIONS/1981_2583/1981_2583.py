classi = input()
vzs = input()

if(classi == "Campeao" and vzs == "06-vezes"):
	print("corinthians".upper())
elif(classi == "Campeao" and vzs == "03-vezes"):
	print("santos".upper())
elif(classi == "Vice-Campeao" and vzs == "01-vez"):
	print("flamengo".upper())
elif(classi == "Vice-Campeao" and vzs == "06-vezes"):
	print("internacional")  
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
