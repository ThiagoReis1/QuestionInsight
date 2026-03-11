unidade = input("Escreva K para kilometros e M para milhas: ")
dist = float(input("Valor da medida: "))
if (unidade.upper() == "K" ):
	print(round(dist/1.60934,2))
else:
	print(round(1.60934*dist,2))