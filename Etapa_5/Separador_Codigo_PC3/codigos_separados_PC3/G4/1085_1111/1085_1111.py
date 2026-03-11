P1 = float(input("Nota da P1:"))
P2 = float(input("Nota da P2:"))
P3 = float(input("Nota da P3:"))
P4 = float(input("Nota da P4:"))
P5 = float(input("Nota da P5:"))

M = (P1 + P2 + P3 + P4 + P5) / 5
if (M >= 6):
	print(round(M, 2))
	print("Aprovado")
else:
	print(round(M, 2))
	print("Reprovado")