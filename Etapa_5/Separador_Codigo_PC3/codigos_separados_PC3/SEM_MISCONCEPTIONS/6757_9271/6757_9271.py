pizza = float(input("Digite o numero de encomendas: "))
if pizza < 3:
	custo = (pizza * 5) + 3
	print(round(custo,2))
elif pizza == 3:
	custo = (pizza * 5) + 3.25
	print(round(custo,2))
else:
	custo = (pizza * 5) + 4.5
	print(round(custo,2))