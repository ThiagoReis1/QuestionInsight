idade=int(input("Digite a sua idade:   "))
peso=float(input("Digite o seu peso:"))
if idade<=20 and idade>0 and peso<=60 and peso>0:
	print("Entradas:",idade,"anos e",round(peso,1),"kg" )
	print("Grupo de risco: 9")
elif idade<=20 and peso>60 and peso<=90:
	print("Entradas:",idade,"anos e",round(peso,1),"kg")
	print("Grupo de risco: 8")
elif idade<=20 and peso>90:
	print("Entradas:",idade,"anos e",round(peso,1),"kg")
	print("Grupo de risco: 7")
elif idade>20 and idade<=50 and peso<=60:
	print("Entradas:",idade,"anos e",round(peso,1),"kg")
	print("Grupo de risco: 6")
elif idade>20 and idade<=50 and peso>60 and peso<=90:
	print("Entradas:",idade,"anos e",round(peso,1),"kg")
	print("Grupo de risco: 5")
elif idade>20 and idade<=50 and peso>90:
	print("Entradas:",idade,"anos e",round(peso,1),"kg")
	print("Grupo de risco: 4")
elif idade>50 and peso<=60:
	print("Entradas:",idade,"anos e",round(peso,1),"kg")
	print("Grupo de risco: 3")
elif idade>50 and peso>60 and peso<=90:
	print("Entradas:",idade,"anos e",round(peso,1),"kg")
	print("Grupo de risco: 2")
elif idade>50 and peso>90:
	print("Entradas;",idade,"anos e",round(peso,1),"kg")
	print("Grupo de risco: 1")
elif idade<=0 or peso<=0:
	print("Entradas:",idade,"anos e",round(peso,1),"kg")
	print("Dados invalidos")