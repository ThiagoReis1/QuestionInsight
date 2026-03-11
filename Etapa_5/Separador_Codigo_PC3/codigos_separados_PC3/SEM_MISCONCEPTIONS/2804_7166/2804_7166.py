taxa = 0.01
dinheiro = float(input("dinheiro: "))
meses = int(input("meses: "))
i = 0
while(i < meses):
	dinheiro = dinheiro + dinheiro*taxa
	print(round(dinheiro, 2))
	i = i + 1
	

