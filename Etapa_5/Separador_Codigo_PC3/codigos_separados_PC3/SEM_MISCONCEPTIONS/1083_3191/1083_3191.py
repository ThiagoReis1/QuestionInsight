nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))
media_da_disciplina = (nota_1 + nota_2 + nota_3) / 3
print(round(media_da_disciplina, 2))
if (media_da_disciplina >= 6.0):
	print("Aprovacao")
else:
	print("Reprovacao")