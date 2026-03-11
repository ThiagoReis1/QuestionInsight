calcular_valor_total_batata(quantidade)
preco_unico_sem_desconto = 0.90
preco_unico_com_desconto = 0.75
desconto_por_dezena = 10

if quantidade < desconto_por_dezena:
	valor_total = quantidade * preco_unico__sem_desconto
	
else:
	valor_total = quantidade * preco_unico_com_desconto

quantidade_batatas = int(input("Digite a quantidade de batatas compradas:"))

valor_total_compra = calcular_valor_total_batatas(quantidade)

print(round(valor_total_compra, 2))