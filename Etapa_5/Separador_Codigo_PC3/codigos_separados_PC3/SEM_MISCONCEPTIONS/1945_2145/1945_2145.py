aminoacido = input("Digite o aminoacido (aspartato/cisteina): ")

C = 12.011
H = 1.00794
N = 14.0067
O = 15.9994
S = 32.066

#peso molecular do aspartato
peso_a = (4 * C) + (6 * H) + N + (4 * O)

#peso molecular do cisteina
peso_c = (3 * C) + (7 * H) + N + (2 * O) + S

if(aminoacido.lower() == "aspartato"):
	print(round(peso_a, 2))
else:
	print(round(peso_c, 2))