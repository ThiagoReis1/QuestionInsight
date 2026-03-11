qtd_hora = float(input("digite quatidade de hora: "))
if (qtd_hora > 20):
	pagamento = qtd_hora - 20 
	pagamento_1 = qtd_hora - pagamento
	pagamento_2 = pagamento_1 * 50
	pagamento_3 = pagamento * 70
	pagamento_4 = pagamento_2 + pagamento_3
	print(round(pagamento_4, 2))
else:
	pagamento_1 = qtd_hora * 50 
	print (round(pagamento_1, 2))