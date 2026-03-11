mol = str(input("Qual o nome do aminoácido desejado? "))
mol = mol.upper()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
if mol == "GLICINA":
	#Glicerina = c2 h5 n o2
	peso = (C*2) + (H*5) + N + (O*2)
if mol == "SERINA":
	#Serina = c3 h7 n o3
	peso = (C*3) + (H*7) + N + (O*3)
print(round(peso, 2))