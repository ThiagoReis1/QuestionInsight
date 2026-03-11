quantas_duplas = int(input("quantas:"))
valor_da_dupla = 32.90

desconto = (quantas_duplas * valor_da_dupla) * (20/100)
valordc = (quantas_duplas*valor_da_dupla) - desconto

if(quantas_duplas > 3):
	print(round(valordc, 2))
else:
	print(round(quantas_duplas * valor_da_dupla, 2))

