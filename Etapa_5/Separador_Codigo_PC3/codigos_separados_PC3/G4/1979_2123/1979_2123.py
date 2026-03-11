camp = input("digite o nome da selecao:").upper()
qts = input("digite quantas vezes foram campeoes:")


if(camp == "CAMPEAO" ) and (qts == "05-vezes"):
	print("BRASIL")
elif(camp == "CAMPEAO") and (qts == "04-vezes"):
	print("ITALIA")
elif(camp == "VICE-CAMPEAO") and (qts == "04-vezes"):
	print("ALEMANHA")
elif(camp == "VICE-CAMPEAO") and (qts == "03-vezes"):
	print("ARGENTINA")
else:
	print("SELECAO NAO IDENTIFICADA")