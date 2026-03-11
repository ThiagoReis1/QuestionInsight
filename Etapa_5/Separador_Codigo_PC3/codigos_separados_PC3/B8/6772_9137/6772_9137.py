valor = float(input("Valor total: "))
pagamento = input("Insira 'D', 'P', 'C1', 'C2': ").upper()

if (pagamento == 'D') or (pagamento == 'P'):
	var1 = valor * 17/100
	desconto = valor - var1

elif (pagamento == 'C1'):
	desconto = valor

elif (pagamento == 'C2'):
	desconto = 108/100 * valor

print(round(desconto, 2))