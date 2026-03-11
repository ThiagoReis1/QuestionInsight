# faça seu código aqui!

qtd = int(input())
custo = 32.9

total = qtd * custo
if qtd > 3:
	total = total - total * 0.2

print(round(total, 2))