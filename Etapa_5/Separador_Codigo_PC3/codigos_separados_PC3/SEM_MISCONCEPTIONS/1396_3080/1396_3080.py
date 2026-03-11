valor_consumido= float(input())
if(valor_consumido <= 300):
	gorjeta= (valor_consumido * (10/100))
else:
	gorjeta= (valor_consumido * (6/100))
valor_total= valor_consumido + gorjeta
print(round(valor_total,2))