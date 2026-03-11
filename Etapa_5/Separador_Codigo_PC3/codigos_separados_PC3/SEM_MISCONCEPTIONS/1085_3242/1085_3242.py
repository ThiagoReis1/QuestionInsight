nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
nota3 = float(input("digite a nota 3: "))
nota4 = float(input("digite a nota 4: "))
nota5 = float(input("digite a nota 5: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if (media >= 6):
	print(round(media, 2))
	print("Aprovacao")
	
else:
	print(round(media, 2))
	print("Reprovacao")