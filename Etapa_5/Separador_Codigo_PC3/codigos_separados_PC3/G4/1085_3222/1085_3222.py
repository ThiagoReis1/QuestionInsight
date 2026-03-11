n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
n4 = float(input("nota 4: "))
n5 = float(input("nota 5: "))

nota = ((n1 + n2 + n3 + n4 + n5) / 5)

if (nota >= 6.0):
	print(round(nota, 2))
	print("Aprovacao")
else:
	print(round(nota, 2))
	print("Reprovacao")