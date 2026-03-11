res = input("flamengo ou vasco?")
titulos = input("penta,tetra ou tri.")

if(res.upper() == "CAMPEAO" and titulos == "04-vezes"):
	print("ITALIA")
elif(res.upper() == "CAMPEAO" and titulos == "05-vezes"):
	print("BRASIL")
elif(res.upper() == "VICE-CAMPEAO" and titulos == "04-vezes"):
	print("ALEMANHA")
elif(res.upper() == "VICE-CAMPEAO" and titulos == "03-vezes"):
	print("ARGENTINA")
else:
	print("SELECAO NAO IDENTIFICADA")