nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

media = (nota1 + nota2 + nota3 + nota4) / 4

if (media >= 5):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao")
	