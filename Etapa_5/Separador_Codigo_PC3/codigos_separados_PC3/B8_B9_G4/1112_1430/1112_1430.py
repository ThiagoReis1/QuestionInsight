s = float(input())
print("Entrada: R$", s)
if s >= 0:
	if s <= 800:
		n = s + (s * 0.5)
		print("Novo salario: R$",round(n,2))
	elif s > 800 and s <= 1000:
		n = s + (s * 0.4)
		print("Novo salario: R$",round(n,2))
	elif s > 1000 and s <= 1200:
		n = s + (s*0.3)
		print("Novo salario: R$",round(n,2))
	elif s > 1200 and s <= 1400:
		n = s + (s*0.2)
		print("Novo salario: R$",round(n,2))
	elif s > 1400 and s <= 1600:
		n = s + (s*0.1)
		print("Novo salario: R$",round(n,2))
	elif s > 1600:
		n = s + (s*0.05)
		print("Novo salario: R$",round(n,2))	
else:
	print("Dado invalido")
	