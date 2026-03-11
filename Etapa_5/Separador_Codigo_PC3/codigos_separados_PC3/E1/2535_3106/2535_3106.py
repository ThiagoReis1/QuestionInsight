valor_a = float(input("Valor depositado no Banco A: "))
valor_b = float(input("Valor depositado no Banco B: "))

taxa_a = float(input("Taxa de juros no Banco A: "))
taxa_b = float(input("Taxa de juros no Banco B: "))

porc_a = taxa_a / 100
porc_b = taxa_b / 100

i = 0

if((valor_a > 0) and (valor_b > 0) and (taxa_a > 0) and (taxa_b > 0) and (valor_a > valor_b) and (taxa_a < taxa_b)):
	while(valor_b < valor_a):
		valor_a = round ( (valor_a + (valor_a * porc_a)), 2 )
		valor_b = round ( (valor_b + (valor_b * porc_b)), 2 )
		i = i + 1
	
	print(i)
		
else:
	print("Dados incorretos")
	