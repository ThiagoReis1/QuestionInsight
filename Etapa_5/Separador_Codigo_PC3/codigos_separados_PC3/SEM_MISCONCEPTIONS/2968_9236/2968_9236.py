preco_lanche = 5.00
preco_salgado = 3.50
preco_refrigerante = 4.00

tipo_item = input("Digite 'L' para lanche ou 'S' para salgado:")
quantidade_item = int(input("Digite a quantidade de lanches ou salgados:"))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes:"))

if tipo_item.upper() == 'L':
	valor_total = (quantidade_item * preco_lanche) + (quantidade_refrigerante * preco_refrigerante)

elif tipo_item.upper() == 'S':
	valor_total = (quantidade_item * preco_salgado) + (quantidade_refrigerante * preco_refrigerante)
	
else:
	print("Tipo de item invalido. Use 'L' lanche ou 'S' para salgado.") 
	exit()

print(round(valor_total, 2))