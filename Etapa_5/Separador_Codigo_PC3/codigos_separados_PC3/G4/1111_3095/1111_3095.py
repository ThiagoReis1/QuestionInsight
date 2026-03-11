ne = float(input())
nf = float(input())
print("Entradas:", ne, "horas extras e", nf, "horas de falta")
if ((ne >= 0) and (nf >= 0)):
	h = ne - (2/3) * nf
	if(h <= 600):
		print("Gratificacao: R$ 100.0")
	elif (600 < h <= 1200):
		print("Gratificacao: R$ 200.0")
	elif (1200 < h <= 1800):
		print("Gratificacao: R$ 300.0")
	elif (1800 < h <= 2400):
		print("Gratificacao: R$ 400.0")
	else:
		print("Gratificacao: R$ 500.0")
else:
	print("Dados invalidos")