# faça seu código aqui!
qnt_peca = int(input("Quantidade de pecas de roupa: "))
preco = 30.0
if qnt_peca < 10:
	total = preco + 3.25

elif qnt_peca == 10:
	total = preco + 4.5

elif qnt_peca > 10:
	total = preco + 6.0
print("total=", round(total, 2))