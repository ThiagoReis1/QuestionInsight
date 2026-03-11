def racao(peso,quantidade):
	custo = quantidade * 5
	return peso - custo


peso_total = float(input())
quantidade_total = float(input())

print(round(racao(peso_total,quantidade_total),2))