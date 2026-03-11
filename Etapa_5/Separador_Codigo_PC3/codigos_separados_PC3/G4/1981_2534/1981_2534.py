a = input("O resultado do time? ").upper()
b = input("Quantas vezes? ").upper()

if(a == "CAMPEAO" and b == "06-VEZES"):
	print("CORINTHIANS")

elif(a == "CAMPEAO" and b == "03-VEZES"):
	print("SANTOS")
		
elif(a == "VICE-CAMPEAO" and b == "01-VEZ"):
	print("FLAMENGO")
	
elif(a == "VICE-CAMPEAO" and b == "06-VEZES"):
	print("INTERNACIONAL")

else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")