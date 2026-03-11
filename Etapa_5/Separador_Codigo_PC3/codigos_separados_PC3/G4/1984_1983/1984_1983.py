c = input("CAMPEAO OU VICE-CAMPEAO: ").upper()
n = input("N VEZES: ")
if(c == 'CAMPEAO' and n == "11-vezes"):
	print("REAL MADRID")
elif(c == 'CAMPEAO' and n == "05-vezes"):
	print("BARCELONA")
elif(c == 'VICE-CAMPEAO' and n == "01-vez"):
	print("CHELSEA")
elif(c == 'VICE-CAMPEAO' and n == "04-vezes"):
	print("MILAN")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
	