# faça seu código aqui!

q_pecas = int(input("quantas pecas: "))

if q_pecas < 10:
	preco = 30 + 3.25
elif q_pecas == 10:
	preco = 30 + 4.50
elif q_pecas > 10:
	preco = 30 + 6.00
print(round(preco,2))