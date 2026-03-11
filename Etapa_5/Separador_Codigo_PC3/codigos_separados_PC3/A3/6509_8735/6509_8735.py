# faça seu código aqui!
horario= float(input("digite o horario do pedido (em horas): "))
quantidade = int(input("digite a quantidade de pratos: "))
preco_prato = 28.50
if horario >= 18:
	valor_total = quantidade * preco_prato*0.8
else:
	valor_total = quantidade * preco_prato
	valor_total = quantidade * preco_prato

valor_total_arredondado = round(valor_total,2)

print(valor_total_arredondado)