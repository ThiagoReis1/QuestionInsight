taxa = 30
consumo = float(input())
if (consumo<=10):
   valor = consumo*3 + taxa
else:
	valor = consumo*3.5 + taxa
print (round(valor,2))