res = input()
qtd = input()

if(res == "Campeao" and qtd == "05-vezes"):
	print("BRASIL")
elif(res == "Campeao" and qtd == "04-vezes"):
	print("ITALIA")
elif(res == "Vice-Campeao" and qtd == "04-vezes"):
	print("ALEMANHA")
elif(res == "Vice-Campeao" and qtd == "03-vezes"):
	print("ARGENTINA")
else:
	print("SELECAO NAO IDENTIFICADA")