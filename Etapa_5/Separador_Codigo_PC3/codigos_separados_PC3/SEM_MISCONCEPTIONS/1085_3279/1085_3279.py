nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())

media = (nota1 + nota2 + nota3 + nota4 + nota5) /5
print(round(media,2))
if(media>= 6):
	print("Aprovacao")
else:
	print("Reprovacao")