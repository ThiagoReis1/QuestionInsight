# faça seu código aqui!
qtde = int(input())
valor = 32.90
if qtde > 3:
	total = valor * qtde
	total = total - total * (20 /100)
else:
	total = valor * qtde
print(round(total, 2))
	
	