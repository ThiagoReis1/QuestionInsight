# Lizandra Kamila Muniz de Andrade
# 21553759
# Faculdade de Tecnologia - FT
# 21.07.16
X = int(input("informe sua idade: "))
Y = float(input("informe seu peso: "))
if(X >= 0 and X <= 130 and Y >= 0.0 and Y <=550.0):
	if (X <= 20 and Y <=60):
		Z = 9
		print("Entradas: ", X, "anos e", Y, "kg")
		print("Grupo de risco: ", Z)
	elif (X <= 20 and Y > 60 and Y <=90):
		Z = 8
		print("Entradas: ", X, "anos e", Y, "kg")
		print("Grupo de risco: ", Z)
	elif (X <=20 and Y > 90):
		Z = 7
		print("Entradas: ", X, "anos e", Y, "kg")
		print("Grupo de risco: ", Z)
	elif(X > 20 and X <= 50 and Y <= 60):
		Z = 6
		print("Entradas: ", X, "anos e", Y, "kg")
		print("Grupo de risco: ", Z)
	elif(X > 20 and X <=50 and Y > 60 and Y <=90):
		Z = 5
		print("Entradas: ", X, "anos e", Y, "kg")
		print("Grupo de risco: ", Z)
	elif(X > 20 and X <=50 and Y > 90):
		Z = 4
		print("Entradas: ", X, "anos e", Y, "kg")
		print("Grupo de risco: ", Z)
	elif(X > 50 and Y <= 60):
		Z = 3
		print("Entradas: ", idade, "anos e", peso, "kg")
		print("Grupo de risco: ", Z)
	elif(X > 50 and Y > 60 and Y <= 90):
		Z = 2
		print("Entradas: ", X, "anos e", Y, "kg")
		print("Grupo de risco: ", Z)
	elif(X > 50 and Y > 90):
		Z = 1
		print("Entradas: ", X, "anos e", Y, "kg")
		print("Grupo de risco: ", Z)
else:
	print("Entradas: ", X, "anos e", Y, "kg")
	print("Dados invalidos")
		