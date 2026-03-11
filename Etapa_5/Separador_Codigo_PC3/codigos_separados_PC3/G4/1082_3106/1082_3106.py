n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))

m=round((n1+n2+n3+n4+n5)/5, 1)

if (m >= 5):
	diga = "Aprovado"
		
else:
	diga = "Reprovado"

print(m)
print(diga)