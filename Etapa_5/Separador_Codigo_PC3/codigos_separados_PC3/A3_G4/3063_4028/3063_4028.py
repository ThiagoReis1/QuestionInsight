PO = float(input("Valor da quantidade de pecas de ouro:"))
nome_armadura = input("(M) para MALHA || (P) para PLACA || (I) para INTEIRA:")
d = input("fator de destreza entre 1 e 8:")
if (nome_armadura == "I"):
	if (PO == 200):
		r = 30*d-20
		print("r")
if (nome_armadura == "M"):
	if (PO == 50):
		r = 15*d-1
if (nome_armadura == "P"):
	if (PO == 100):
		r = 20*d-18
	else:
		print("PO insuficiente")
print("PO insuficiente")
	

	
	


