custo = float(input("preco de custo"))
if custo <= 50:
	print(round(custo + custo,2))
elif custo >50 and custo < 100:
	print(round(custo + custo*50/100,2))
elif custo >100 and custo < 500:
	print(round(custo + custo*40/100,2))
else:
	print(round(custo + custo*30/100,2))