salario = float(input())

print('Entrada: R$ ', salario)


if salario > 0:
	if 0 <= salario <= 800:
		ns = salario + salario * 0.5
		print('Novo salario: R$ ', round(ns, 2))
	elif 800 < salario <= 1000:
		ns = salario + salario * 0.4
		print('Novo salario: R$ ', round(ns, 2))
	elif 1000 < salario <= 1200:
		ns = salario + salario * 0.3
		print('Novo salario: R$ ', round(ns, 2))
	elif 1200 < salario <= 1400:
		ns = salario + salario * 0.2
		print('Novo salario: R$ ', round(ns, 2))
	elif 1400 < salario <= 1600:
		ns = salario + salario * 0.10
		print('Novo salario: R$ ', round(ns, 2))
	elif salario > 1600:
		ns = salario + salario * 0.05
		print('Novo salario: R$ ', round(ns, 2))
else:
	print('Dado invalido')