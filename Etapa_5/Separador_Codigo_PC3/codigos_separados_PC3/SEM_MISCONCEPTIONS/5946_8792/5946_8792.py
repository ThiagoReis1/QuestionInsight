item = input("Lanche ou pizza? ")
qdd = int(input("Quandidade de Lanches ou pizzas: "))
refri = int(input("Qdd de refri"))

conta1 = qdd*4.50 + refri*3
conta2 = qdd*6 + refri*3

if item == "P":
	print(round(conta1, 2))
else:
	print(round(conta2,2))