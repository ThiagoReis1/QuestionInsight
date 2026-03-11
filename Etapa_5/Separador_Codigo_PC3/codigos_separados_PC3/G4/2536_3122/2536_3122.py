c = float(input("Valor da casa: "))
d = float(input("Valor inicial depositado: "))
m = float(input("Deposito mensal fixo: "))
j = float(input("Taxa de juros: "))

s = d
i = 0
juros = j / 100

if (c > 0) and (d > 0) and (m > 0) and (j > 0):
	while (s <= c):
		i = i + 1
		s = s + (s * juros) + m
	print(round(i, 2))
else:
	print("Dados incorretos")
