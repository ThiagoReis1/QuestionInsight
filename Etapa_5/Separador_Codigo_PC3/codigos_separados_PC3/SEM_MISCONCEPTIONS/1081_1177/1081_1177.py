nota_1 = float(input("Nota da prova 1: "))
nota_2 = float(input("Nota da prova 2: "))
nota_3 = float(input("Nota da prova 3: "))
nota_4 = float(input("Nota da prova 4: "))

media = (((nota_1 + nota_2 + nota_3 + nota_4) / 4), 2)

if (media >= 5.0):
	print(round(media, 1))
	print("Aprovado")
else:
	print(round(media, 1))
	print("Reprovado")
