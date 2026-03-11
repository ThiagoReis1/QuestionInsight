valor = float(input("Valor de vendas: "))

if (valor > 1000.00):
	excedente = valor - 1000.00
	comissao = (0.05 * 1000.00) + ((10/100) * excedente)
else:
	comissao = 0.05 * valor
	
print(round(comissao,2))