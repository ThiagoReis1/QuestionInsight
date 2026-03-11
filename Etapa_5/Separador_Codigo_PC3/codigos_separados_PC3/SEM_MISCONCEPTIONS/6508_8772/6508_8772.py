# faça seu código aqui!
qtde = int(input())
combo = 50
preco = qtde * combo
desconto = 0.12 * preco

if qtde > 4:
	total = preco - desconto
	print(round(total,2))
else:
	print(round(preco, 2))
