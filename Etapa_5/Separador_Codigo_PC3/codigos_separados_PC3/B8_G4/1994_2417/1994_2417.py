nome = input("")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
if (nome.lower != "histidina") and (nome.lower() != "leucina") and (nome.lower() != "lisina"):
	print("Entrada:", nome.lower())
	print("Dado Invalido")		
else:
	if nome.lower() == "histidina" :
		peso_mol = C * 6 + H * 10 + N * 3 + O * 2
		print(round(peso_mol, 2))
	elif nome.lower() == "leucina" :
		peso_mol = C * 6 + H * 13 + N + O * 2
		print(round(peso_mol, 2))
	elif nome.lower() == "lisina" :
		peso_mol = C * 6 + H * 15 + N * 2 + O * 2
		print(round(peso_mol, 2))