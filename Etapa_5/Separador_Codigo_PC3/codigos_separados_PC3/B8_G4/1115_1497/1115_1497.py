#Universidade Federal do Amazonas
#Jadson Brendo Pantoja dos Santos - 21601585
#Avaliação Parcial 03 - 21/07/2016
X = float(input("Salário atual: "))
Y = int(input("código do cargo: "))
print("Entradas: R$", X,"e codigo", Y)
if(X >= 0):
	if(Y >= 101 and Y <= 104):
		if(Y == 101):
			Z = X * (100.80/100)
		elif(Y == 102):
			Z = X * (100.65/100)
		elif(Y == 103):
			Z = X *  (100.60/100)
		elif(Y == 104):
			Z = X * (100.055/100)
		print("Novo salario: R$", round(Z,2))
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")