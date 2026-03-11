s = float(input("qual o salario do cidadão?"))

if s > 0:
	if s <= 800:
		a = s + (s * 0.5)
	elif s > 800 and s <= 1000:
		a = s + (s * 0.4)
	elif s > 1000 and s <= 1200:
		a = s + (s * 0.3)
	elif s > 1200 and s <= 1400:
		a = s + (s * 0.2)
	elif s > 1400 and s <= 1600:
		a = s + (s * 0.1)
	elif s > 1600:
		a = s + (s * 0.05)
	s = round(s, 2)
	a = round(a, 2)
	print("Entrada: R$", s)
	print("Novo salario: R$", a)
else:
	print("Entrada: R$", s)
	print("Dado invalido")