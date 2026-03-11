n1 = float(input("informe a nota 1: "))
n2 = float(input("informe a nota 2: "))
n3 = float(input("informe a nota 3: "))
n4 = float(input("informe a nota 4: "))
n5 = float(input("informe a nota 5: "))
media = (n1 + n2 + n3 + n4 + n5) / 5

if (media >= 7):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao")
