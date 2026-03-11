# faça seu código aqui!
encomendas= int(input("Digite o numero de pizza encomendadas: "))

if (encomendas< 3):
	taxa= 5 * encomendas
	total= taxa + 3
	print("total=",round(total,2))
elif (encomendas == 3):
	taxa= 5 * encomendas
	total= taxa + 3.25
	print("total=",round(total,2))
else:
	taxa= 5 * encomendas
	total= taxa + 4.5
	print("total=",round(total,2))
