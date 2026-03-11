vogais = "A E I O U".split()

etiqueta = input().upper()

preco = 0
i = 0
tam = len(etiqueta)
while i < tam:
	if etiqueta[i] in vogais:
		preco += 0.15
	else:
		preco += 0.17
	i += 1

print(round(preco, 2))