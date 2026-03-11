
s = float(input("salario atual:"))

if s >= 0:
	if s > 0 and s <= 800:
		print("Novo salario: R$", round(( s + ( s * 0.5)), 2))
	elif s > 800 and s <= 1000:
		print("Novo salario: R$", round(( s + ( s * 0.4)), 2))
	elif s > 1000 and s <= 1200:
		print("Novo salario: R$", round(( s + ( s * 0.3)), 2))
	elif s > 1200 and s <= 1400:
		print("Novo salario: R$", round(( s + ( s * 0.2)), 2))
	elif s > 1400 and s <= 1600:
		print("Novo salario: R$", round(( s + ( s * 0.1)), 2))
	elif s > 1600:
		print("Novo salario: R$", round(( s + ( s * 0.05)), 2))
	else:
		print("Dado invalido")
		
else:
	print("Dado invalido")
		