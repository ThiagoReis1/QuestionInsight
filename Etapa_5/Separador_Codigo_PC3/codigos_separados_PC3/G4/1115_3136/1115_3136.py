s = float(input("Salario: "))
c = int(input("Codigo: "))


if(c == 101):
	t = (0.80 / 100) * s
	n = s + t
	print("Entradas: R$", s, "e codigo", c)
	print("Novo salario: R$",round(n, 2))
elif(c == 102):
	t = (0.65 / 100) * s
	n = s + t
	print("Entradas: R$", s, "e codigo", c)
	print("Novo salario: R$",round(n, 2))
elif(c == 103):
	t = (0.60 / 100) * s
	n = s + t
	print("Entradas: R$", s, "e codigo", c)
	print("Novo salario: R$",round(n, 2))
elif(c == 104):
	t = (0.55 / 100) * s
	n = round(s + t, 2)
	print("Entradas: R$", s, "e codigo", c)
	print("Novo salario: R$",round(n, 2))
else:
	print("Entradas: R$", s, "e codigo", c)
	print("Dados invalidos")
	
	