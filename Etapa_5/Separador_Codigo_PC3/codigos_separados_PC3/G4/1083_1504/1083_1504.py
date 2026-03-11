p1 = float(input("nota1:"))
p2 = float(input("nota2:"))
p3 = float(input("nota3:"))

nota = (p1 + p2 + p3)/ 3

print(round(nota, 2))
if(nota >= 6):
	print("Aprovacao")
else:
	print("Reprovacao")

