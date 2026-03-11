cliente = input("Sim ou Nao").upper()
cont = 0
while cliente != "S":
	if cliente == "SIM":
		cont=cont+1
	cliente = input("Sim ou Nao").upper()
print(cont)