x = int(input("Idade do individuo: "))
y = float(input("Peso da pessoa: "))

if (x > 0 and x <= 20 and y > 0 and y <= 60):
	print("Entradas:" ,x,"anos e",round(y,1),"kg")
	print("Grupo de risco: 9")
elif (x > 0 and x <= 20 and y > 60 and y <= 90):
	print("Entradas:",x ,"anos e", round(y,1) ,"kg")
	print("Grupo de risco: 8")
elif (x > 0 and x <= 20 and y > 90):
	print("Entradas:", x, "anos e", round(y,1), "kg")
	print("Grupo de risco: 7")
elif (x > 0 and x > 20 and x <= 50 and y <= 60):
	print("Entradas:", x, "anos e", round(y,1),"kg")
	print("Grupo de risco: 6")
elif (x > 0 and x > 20 and x <= 50 and y > 60 and y <= 90):
	print("Entradas:", x, "anos e", round(y,1), "kg")
	print("Grupo de risco: 5")
elif (x > 0 and x > 20 and x <= 50 and y > 90):
	print("Entradas", x, "anos e", round(y,1), "kg")
	print("Grupo de risco: 4")
elif (x > 0 and x > 50 and y <= 60):
	print("Entradas" ,x, "anos e", round(y,1), "kg")
	print("Grupo de risco: 3")
elif (x > 0 and x > 50 and y > 60 and y <= 90):
	print("Entradas", x, "anos e", round(y,1), "kg")
	print("Grupo de risco: 2")
elif (x > 0 and x > 50 and y > 90):
	print("Entradas", x ,"anos e", round(y,1), "kg")
	print("Grupo de risco: 1")
elif( x < 0 or x > 130 and y < 0 or y > 550):
	print("Dados invalidos")