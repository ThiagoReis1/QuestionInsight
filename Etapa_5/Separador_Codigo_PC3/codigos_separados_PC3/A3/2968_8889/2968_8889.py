escolha = input(" ")
L = 5.00
salgado = 3.50
refrigerante = 4.00
qtde = (int(input()))

if escolha == "S":
	lanche = int(input())
	refrigerante = int(input())
	total = qtde * 5 + lanche + 4
else:
	lanche = int(input())
	total= 4.00 + lanche + refrigerante * 4
	print(round(total,2))

