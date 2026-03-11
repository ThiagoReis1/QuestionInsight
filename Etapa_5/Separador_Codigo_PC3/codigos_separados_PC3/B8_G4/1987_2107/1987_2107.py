O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794

mol = input("digite o aminoacido: ").upper()


if(mol!="ALANINA" and mol!="VALINA" and mol!="TIROSINA"):
	print("Entrada:",mol)
	print("Dado Invalido")
	
else:
	if(mol=="ALANINA"): 
		print(round(3*C + 7*H + N + 3*O, 2))
	if(mol=="VALINA"): 
		print(round(5*C + 11*H + N + 2*O, 2))
	if(mol=="TIROSINA"): 
		print(round(9*C + 11*H + N + 3*O, 2))