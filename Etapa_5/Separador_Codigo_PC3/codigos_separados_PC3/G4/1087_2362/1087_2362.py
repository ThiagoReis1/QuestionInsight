n1 = float(input(":"))
n2 = float(input(":"))
n3 = float(input(":"))
n4 = float(input(":"))

media = (n1 + n2 + n3 + n4) / 4

if (media >= 7):
	print(round(media, 2))
	print("Aprovado")
else:
	print(round(media, 2))
	print("Reprovado")