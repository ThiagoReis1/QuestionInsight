# faça seu código aqui!
idade = int(input("digite um numero:"))
preco = 20.00

if idade < 12:
	total1 = preco + 1.25
	print(round(total1, 2))
elif idade == 12:
	total2 = preco + 2.25
	print(round(total2, 2))
else:
	total3 = preco + 3.25
	print(round(total3, 2))
