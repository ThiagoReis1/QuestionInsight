r = input("digite o valor do resultado:").upper()
q = input("digite o valor das vezes:").upper()

if(r == "CAMPEAO" and q == "05-VEZES"):
	print("BRASIL")
elif(r == "CAMPEAO" and q == "04-VEZES"):
	print("ITALIA")
elif(r == "VICE-CAMPEAO" and q == "04-VEZES"):
	print("ALEMANHA")
elif(r == "VICE-CAMPEAO" and q == "03-VEZES"):
	print("ARGENTINA")
else:
	print("SELECAO NAO IDENTIFICADA")
