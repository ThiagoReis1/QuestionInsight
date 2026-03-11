vendas = float(input())

calculo = vendas * 5 / 100
maior = calculo * 10 / 100
aci = vendas - (calculo + maior)

if(vendas >= 1000):
	print(round(aci, 2))
else:
	print(round(maior, 2))
