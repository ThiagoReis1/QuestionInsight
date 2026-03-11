# Entrada 

vendas = float(input("Valor de vendas:"))

# Condicao

if vendas <= 1000:
	comissao = vendas * (5/100)
else:
	comissao = 1000 * (5/100) + ((vendas - 1000)* (10/100))
	
# Saida 

print(round(comissao,2))