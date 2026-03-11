n1 = float(input("digite nota 1: "))
n2 = float(input("digite nota 2: "))
n3 = float(input("digite nota 3: "))
media = ((n1 + n2 + n3) / 3)
print(round(media , 2))
if (media >= 6):
	print("Aprovacao")
else:
	print("Reprovacao")