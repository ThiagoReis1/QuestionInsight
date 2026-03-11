nome = input("Nome do aminoácido (Glicina ou Serina): ")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if(nome.upper() == "GLICINA"):
	pesoMol = 2 * C + 5 * H + N + 2 * O
	
if(nome.upper() == "SERINA"):
	pesoMol = 3 * C + 7 * H + N + 3 * O

print(round(pesoMol, 2))