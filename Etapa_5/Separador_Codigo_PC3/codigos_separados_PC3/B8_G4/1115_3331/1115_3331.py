sa= float(input("Salario Atual: "))
c= int(input("codigo: "))

if (c == 101 or c == 102 or c == 103 or c == 104) and (sa > 0):
	print("Entrada: R$", sa,"e codigo", c)
	if (c == 101):
		r= sa*0.80
		r2= r/100
		r3= r2 + sa
		print("Novo salario: R$", round(r3, 2))
	elif (c == 102):
		r= sa*0.65
		r2= r/100
		r3= r2 + sa
		print("Novo salario: R$", round(r3, 2))
	elif (c == 103):
		r= sa*0.60
		r2= r/100
		r3= r2 + sa
		print("Novo salario: R$", round(r3, 2))
	elif (c == 104):
		r= sa*0.55
		r2= r/100
		r3= r2 + sa
		print("Novo salario: R$", round(r3, 2))
else:
	print("Entrada: R$", sa,"e codigo", c)
	print("Dados invalidos")