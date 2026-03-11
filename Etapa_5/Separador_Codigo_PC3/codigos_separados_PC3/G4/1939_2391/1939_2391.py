nome = input("Nome do aminoacido: ")

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
Asparagina = 4*C + 8*H + 2*N + 3*O
Triptofano = 11*C + 11*H + 2*N + 2*O

if (nome.upper() == "ASPARAGINA"):
	print(round(Asparagina, 2))
if (nome.upper() == "TRIPTOFANO"):
	print(round(Triptofano, 2))