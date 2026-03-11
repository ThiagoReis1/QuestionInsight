X = input("Nome do aminoácido:").upper()

O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794

if (X == "GLUTAMINA"):
	p = (5 * C) + (8 * H) + (N) + (4 * O)
	print(round( p , 2))
elif(X == "SERINA"):
	p = (3 * C) + (7 * H) + (N) + (3 * O)
	print(round( p , 2))
elif(X == "TREONINA"):
	p = (4 * C) + (9 * H) + (N) + (3 * O)
	print(round( p , 2))
else:
	print("Entrada:", X)
	print("Dado Invalido")