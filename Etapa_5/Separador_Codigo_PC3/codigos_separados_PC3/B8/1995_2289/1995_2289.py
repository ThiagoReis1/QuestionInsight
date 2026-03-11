molecula = input("qual a molecula? ").lower()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

peso_molecular1 = ((4*C) + (6*H) + N + (4*O))
peso_molecular2 = ((3*C) + (7*H) + N + (O*2) + S)
peso_molecular3 = ((5*C) + (11*H) + N + (O*2) + S)

if (molecula != "aspartato" and molecula != "cisteina" and molecula != "metionina"):
	print("Entrada: " + molecula)
	print("Dado Invalido")
else:
	if (molecula == "aspartato"):
		print(round(peso_molecular1, 2))
	elif (molecula == "cisteina"):
		print(round(peso_molecular2, 2))
	elif (molecula == "metionina"):
		print(round(peso_molecular3, 2))