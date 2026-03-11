p1 = float(input("prova1: "))
p2 = float(input("prova2: "))
p3 = float(input("prova3: "))
media = (p1 + p2 + p3)/3
if (media >= 6):
	print(round(media, 2), "Aprovacao")
else:
	print(round(media, 2), "Reprovacao")