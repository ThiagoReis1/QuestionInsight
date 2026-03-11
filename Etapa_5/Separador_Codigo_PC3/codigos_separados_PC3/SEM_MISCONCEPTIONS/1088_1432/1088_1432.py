nota1 = float(input("Informa a nota 1:"))
nota2 = float(input("Informa a nota 2:"))
nota3 = float(input("Informa a nota 3:"))
nota4 = float(input("Informa a nota 4:"))
nota5 = float(input("Informa a nota 5:"))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(round(media,2))
if (media >= 7.0):
	print("Aprovacao")
else:
	print("Reprovacao")