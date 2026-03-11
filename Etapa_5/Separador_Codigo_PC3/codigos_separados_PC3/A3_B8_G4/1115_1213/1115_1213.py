sa = float(input("entrada:"))
co = int(input("codigo:"))
ns = 0
if (co != 101 and co != 102 and co != 103 and co != 104) or (sa<0):
	print("Entradas: R$",sa,"e codigo",co)
	print("Dados invalidos")
elif(co == 101):
	ns = sa + (sa*0.0080)
	print("Entradas: R$",sa,"e codigo",co)
	print("Novo salario:","R$",round(ns,2))	
elif(co == 102):
	ns = sa + (sa*0.0065)
	print("Entradas: R$",sa,"e codigo",co)
	print("Novo salario:","R$",round(ns,2))	
elif(co == 103):
	ns = sa + (sa*0.006)
	print("Entradas: R$",sa,"e codigo",co)
	print("Novo salario:","R$",round(ns,2))
elif(co == 104):
	ns = sa + (sa*0.0055)
	print("Entradas: R$",sa,"e codigo",co)
	print("Novo salario:","R$",round(ns,2))

	
