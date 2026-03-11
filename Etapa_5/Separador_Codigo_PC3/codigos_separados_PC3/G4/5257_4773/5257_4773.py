pc1 = float(input("valor do preco de custo: "))

if pc1 <= 50:
	pf = pc1 + (pc1*1)
	print(round(pf, 2))
elif pc1 <= 100:
	pf = pc1 + (pc1*0.50)
	print(round(pf, 2))
elif pc1 <= 500:
	pf = pc1 + (pc1*0.40)
	print(round(pf, 2))
else:
	pf = pc1 + (pc1*0.30)
	print(round(pf, 2))