# faça seu código aqui!
tempo = float(input())
if tempo < 2:
	preco = 1.25 + 5
elif tempo == 2:
	preco = 2.25 + 5
else:
	preco = 3.25 + 5

print(round(preco, 2))