H1 = float(input("horas extras: "))
N1 = float(input("horas faltadas: "))

I = H1 - N1*(2/3)

if((H1>=0) and (N1>=0)):
	if(I>2400):
		print("Entradas:", H1, "horas extras e", N1, "horas de falta")
		print("Gratificacao: R$", round(500.00, 2))
	elif((I>1800) and (I<=2400)):
		print("Entradas:", H1, "horas extras e", N1, "horas de falta")
		print("Gratificacao: R$", round(400.00, 2))
	elif((I>1200) and (I<=1800)):
		print("Entradas:", H1, "horas extras e", N1, "horas de falta")
		print("Gratificacao: R$", round(300.00, 2))
	elif((I>600) and (I<=1200)):
		print("Entradas:", H1, "horas extras e", N1, "horas de falta")
		print("Gratificacao: R$", round(200.00, 2))
	else:
		print("Entradas:", H1, "horas extras e", N1, "horas de falta")
		print("Gratificacao: R$", round(100.00, 2))
else:
	print("Entradas:", H1, "horas extras e", N1, "horas de falta")
	print("Dados invalidos")