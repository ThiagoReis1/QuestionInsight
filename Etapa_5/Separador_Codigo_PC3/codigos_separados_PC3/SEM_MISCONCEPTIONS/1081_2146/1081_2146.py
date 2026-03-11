nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
geral = nota1 + nota2 + nota3 + nota4
media = geral / 4

if (media >= 5):
	print(round(media, 2))
	print("Aprovacao")
	
else:
	print(round(media, 2))
	print("Reprovacao")