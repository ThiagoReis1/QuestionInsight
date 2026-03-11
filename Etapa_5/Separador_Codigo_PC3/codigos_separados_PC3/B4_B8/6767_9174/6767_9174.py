valor_compra = float(input("valor compra: "))
pagamento = input("forma pagamento: ").upper()

if pagamento == "D":
	valor_total = valor_compra * 0.12
	valor_final = valor_compra - valor_total
	print(round(valor_final,2))
	
elif pagamento == "P":
	valor_total = valor_compra * 0.12
	valor_final = valor_compra - valor_total
	print(round(valor_final,2))
	
elif pagamento == "C1":
	print(round(valor_compra,2))

elif pagamento == "C2":
	valor_total = valor_compra * 1.07
	print(round(valor_total,2))