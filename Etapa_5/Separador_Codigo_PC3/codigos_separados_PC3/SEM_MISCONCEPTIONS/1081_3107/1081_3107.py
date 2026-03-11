nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())
nota_4 = float(input())

media = ((nota_1 + nota_2 + nota_3 + nota_4) / 4)

if media >= 5.0:
	print(round(media, 2))
	print("Aprovacao")
else:
	print(round(media, 2))
	print("Reprovacao")