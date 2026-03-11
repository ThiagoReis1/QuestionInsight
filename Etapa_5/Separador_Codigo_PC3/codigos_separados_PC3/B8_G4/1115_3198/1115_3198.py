sa = float(input())
co = int(input())

if ((sa <= 0) and (co != 101) and (co != 102) and (co != 103) and (co != 104)):
	print("Entradas:", "R$", sa, "e codigo", co)
	print("Dados invalidos")
	
elif ((co == 101)):
	r = (sa * 0.8)
	ns = (sa + r)
	print("Entradas:", "R$", sa, "e codigo", co)
	print("Novo salario:", "R$", round(ns,2))
	
elif ((co == 102)):
	r = (sa * 0.65)
	ns = (sa + r)
	print("Entradas:", "R$", sa, "e codigo", co)
	print("Novo salario:", "R$", round(ns,2))

elif ((co == 103)):
	r = (sa * 0.6)
	ns = (sa + r)
	print("Entradas:", "R$", sa, "e codigo", co)
	print("Novo salario:", "R$", round(ns,2))

elif ((co == 104)):
	r = (sa * 0.55)
	ns = (sa + r)
	print("Entradas:", "R$", sa, "e codigo", co)
	print("Novo salario:", "R$", round(ns,2))


