idade=int(input())
peso=float(input())

if not(idade>=0) or not(idade<=130) or not(peso>=0.0) or not(peso<=550.0):
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Dados invalidos")
elif idade<=20 and (peso<=60):
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 9")
elif idade<=20 and (peso>60 or peso<=90):
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 8")
elif idade<=20 and peso>90:
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 7")
elif (idade>20 or idade<=50) and peso<=60:
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 6")
elif (idade>20 or idade<=50) and (peso>60 or peso<=90):
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 5")
elif (idade>20 or idade<=50) and peso>90:
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 4")
elif idade>50 and peso<=60:
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 3")
elif idade>50 and (peso>60 or peso<=90):
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 2")
elif idade>50 and peso>90:
	print("Entradas: ", idade, "anos e", peso,"kg")
	print("Grupo de risco: 1")
	

