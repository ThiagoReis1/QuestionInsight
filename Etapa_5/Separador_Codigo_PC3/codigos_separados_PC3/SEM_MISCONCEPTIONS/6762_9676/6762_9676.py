# faça seu código aqui!
idade = int(input("digite sua idade"))
if idade < 12:
	preco = 20 + 1.25
	print(round(preco,2))
elif idade == 12:
	preco = 20 + 2.25
	print(round(preco,2))
else:
	preco = 20 + 3.25
	print(round(preco,2))