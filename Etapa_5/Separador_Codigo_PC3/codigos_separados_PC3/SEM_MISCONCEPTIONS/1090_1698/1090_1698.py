#Marcos Felipe Melo de Lima - 21554017
#Avaliacao 2
compra1 = float(input("Digite o valor da 1 compra:"))
compra2 = float(input("Digite o valor da 1 compra:"))
compra3 = float(input("Digite o valor da 1 compra:"))
compra4 = float(input("Digite o valor da 1 compra:"))
limite = float(input("Digite o valor limite do cartao:"))

compras_total = compra1 + compra2 + compra3 + compra4

if(compras_total <= limite):
	print(round(compras_total, 2))
	print("Sim")
else:
	print(round(compras_total, 2))
	print("Nao")