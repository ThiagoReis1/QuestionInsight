compra_1= float(input("Digite o valor da primeira compra: "))
compra_2= float(input("Digite o valor da segunda compra: "))
compra_3= float(input("Digite o valor da terceira compra: "))
compra_4= float(input("Digite o valor da quarta compra: "))
limite= float(input("Digite o limite do cartao:"))
total= (compra_1 + compra_2 + compra_3 + compra_4)
print(round(total,2))
if (total <= limite):
		print ("Sim")
else:
		print("Nao")
	