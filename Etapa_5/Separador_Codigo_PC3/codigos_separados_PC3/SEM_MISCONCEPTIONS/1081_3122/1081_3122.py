nota1 = float(input("Nota1: "))
nota2 = float(input("Nota2: "))
nota3 = float(input("Nota3: "))
nota4 = float(input("Nota4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if(media >= 5.0):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao")
