
atk = input("Tipo de ataque: ")
dado = int(input("valor do dado: "))
tpc = int(input("turnos: "))
if(atk == "cuspe"):
	print(2*dado*tpc)
if(atk == "cauda"):
	print(1*dado*tpc)
	
	