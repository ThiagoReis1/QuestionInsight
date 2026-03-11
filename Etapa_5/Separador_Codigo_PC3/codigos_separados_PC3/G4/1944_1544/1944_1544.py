O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
molecula = input("entre com o aminoacido: ")
if (molecula.lower() == "leucina"):
	peso = ((6 * C) + (13 * H) + (N * 1) + (O * 2))
else:
	peso = ((6 * C) + (15 * H) + (2 * N) + (2 * O))
print(round(peso,2))