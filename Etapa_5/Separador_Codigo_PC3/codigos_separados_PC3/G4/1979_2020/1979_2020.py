
r = input("resultado da selecao: ")
q = input("quantas vezes alcancou o resultado: ")

if(r=="Campeao") and (q == "05-vezes"):
	print("BRASIL")
elif(r=="Campeao") and (q == "04-vezes"):
	print("ITALIA")
elif(r=="Vice-Campeao") and (q=="04-vezes"):
	print("ALEMANHA")
elif(r=="Vice-Campeao") and (q=="03-vezes"):
	print("ARGENTINA")
else:
	print("SELECAO NAO IDENTIFICADA")
