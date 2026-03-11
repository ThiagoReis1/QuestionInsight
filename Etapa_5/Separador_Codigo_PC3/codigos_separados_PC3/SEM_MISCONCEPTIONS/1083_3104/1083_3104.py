nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (round((nota1 + nota2 + nota3) / 3, 2))
print(media)

if (media >= 6.0):
	print("Aprovacao")
else:
	print("Reprovacao")
	
