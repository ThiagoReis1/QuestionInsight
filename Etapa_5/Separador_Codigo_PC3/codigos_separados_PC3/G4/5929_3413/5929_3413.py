def conta(volume):
	custo = (volume * 0.37) + 15
	taxa = custo * 0.35
	return custo + taxa

v = float(input())
custo_total = conta(v)

print(round(custo_total,2))