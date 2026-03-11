mensalidade = float(input("Digite: "))
criancas = int(input("digite: "))

if (criancas == 1):
	d = mensalidade * 10 / 100
	e = mensalidade - d
	vt = e * criancas
	print(round(vt, 2))
elif (criancas == 2):
	d = mensalidade * 30 / 100
	e = mensalidade - d
	vt = e * criancas
	print(round(vt, 2))
elif (criancas >= 3):
	d = mensalidade * 40 / 100
	e = mensalidade - d
	vt = e * criancas
	print(round(vt, 2))
