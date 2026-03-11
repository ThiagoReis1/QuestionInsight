O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794
molecula = input("Cisteina, Isoleucina ou Metionina: ").lower()
if (molecula == "cisteina"):
	mol = ((3 * C) + (7 * H) + (1 * N) + (2 * O) + (1 * S))
	print(round(mol,2))
elif (molecula == "isoleucina"):
	mol = ((6 * C) + (13 * H) + (1 * N) + (2 * O))
	print(round(mol,2))
elif (molecula == "metionina"):
	mol = ((5 * C) + (11 * H) + (1 * N) + (2 * O) + (1 * S))
	print(round(mol,2))
else:
	print("Entrada:", molecula)
	print("Dado Invalido")