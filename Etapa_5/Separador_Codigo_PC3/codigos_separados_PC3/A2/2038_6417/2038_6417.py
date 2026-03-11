p = input("O atendimento foi satisfatorio? ").upper()

clientes = 0 # Clientes que responderam sim
while (p != "S"):
	if(p == "SIM"):
		clientes = clientes + 1
	else:
		clientes = clientes
	p = input("O atendimento foi satisfatorio? ").upper()
	
print(clientes)