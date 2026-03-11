n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))
ma = abs(n1 + n2 + n3 + n4 + n5)/5
if	(ma >= 5):
	msg = "Aprovado"
else:
	msg = "Reprovado"
print(round(ma, 1))
print(msg)