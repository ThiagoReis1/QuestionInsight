hectaria = float(input("Digite a área a ser fertilizada: (em hectarias) "))
if(hectaria <= 10000):
	custo_total= hectaria*5
	print(custo_total)
else:
	custo_total= hectaria-10000
	custo_total = custo_total*4 + 10000*5
	print(round(custo_total, 2))