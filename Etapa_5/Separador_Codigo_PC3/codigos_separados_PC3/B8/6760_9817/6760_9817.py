# faça seu código aqui!
roupas= int(input("Digite a quantidade de roupas:"))

if roupas < 10:
	total= float(30 + 3.25)
	print(round(total,2))
elif roupas == 10:
	total= float(30 + 4.5)
	print(round(total, 2))
elif roupas > 10:
	total = float(30 + 6)
	print(round(total, 2))
	