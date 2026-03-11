resposta = input("Sim ou Nao: ").upper()
sim = 0
while resposta != "S":
	if resposta == "SIM":
		sim = sim + 1
	resposta = input("Sim ou Nao").upper()	
print(sim)