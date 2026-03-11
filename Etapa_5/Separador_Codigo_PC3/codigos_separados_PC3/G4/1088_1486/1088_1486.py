n1 = float(input("Nota da primeira prova: "))
n2 = float(input("Nota da segunda prova: "))
n3 = float(input("Nota da terceira prova: "))
n4 = float(input("Nota da quarta prova: "))
n5 = float(input("Nota da quinta prova: "))

media = (n1 + n2 + n3 + n4 + n5) / 5

if(media >= 7):
	print(round(media, 2))
	print("Aprovacao")

else:
	print(round(media, 2))
	print("Reprovacao")