sa = float(input("Salario Atual: "))
#
if(sa > 0 and sa <= 800):
	ns = (sa * 0.5) + sa
	print("Novo salario: R$", round(ns , 2))
elif(sa > 800 and sa <= 1000):
	ns = (sa * 0.4) + sa
	print("Novo salario: R$", round(ns , 2))
elif(sa > 1000 and sa <= 1200):
	ns = (sa * 0.3) + sa
	print("Novo salario: R$", round(ns , 2))
elif(sa > 1200 and sa <= 1400):
	ns = (sa * 0.2) + sa
	print("Novo salario: R$", round(ns , 2))
elif(sa > 1400 and sa <= 1600):
	ns = (sa * 0.1) + sa
	print("Novo salario: R$", round(ns , 2))
elif(sa > 1600):
	ns = (sa * 0.05) + sa
	print("Novo salario: R$", round(ns , 2))
else:
	print("Dado invalido")