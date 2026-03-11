valor = float(input())
if(valor <= 300):
	total = valor + (valor * 0.1)
else:
	total = valor + (valor * 0.06)
print(round(total, 2))