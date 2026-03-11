compra_1 = float (input("digite o valor da primeira compra"))
compra_2 = float (input("digite o valor da segunda compra"))
compra_3 = float (input("digite o valor da terceira compra"))
compra_4 = float (input("digite o valor da quarta compra"))
limite = float (input("informe o valor do limite do cartão de credito"))
valor_total = compra_1 + compra_2 + compra_3 + compra_4
print (round(valor_total,2)) 
if valor_total <= limite:
	print ("Sim")
else:
	print ("Nao")