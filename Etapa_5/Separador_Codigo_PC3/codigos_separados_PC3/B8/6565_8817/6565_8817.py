# faça seu código aqui!
encomendas = int(input())

if encomendas < 10:
	t = 50 + 5.50
	print("total=",round(t, 2))
elif encomendas == 10:
	t = 50 + 7.75
	print("total=",round(t, 2))
elif encomendas > 10:
	t = 50 + 10.0
	print("total=",round(t, 2))
