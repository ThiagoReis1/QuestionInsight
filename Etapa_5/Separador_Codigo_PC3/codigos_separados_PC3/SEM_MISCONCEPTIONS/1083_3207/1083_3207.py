nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota = (nota1+nota2+nota3)/3
if (nota>= 6.0):
	print(round(nota,2))
	print("Aprovacao")
else:
	print(round(nota,2))
	print("Reprovacao")