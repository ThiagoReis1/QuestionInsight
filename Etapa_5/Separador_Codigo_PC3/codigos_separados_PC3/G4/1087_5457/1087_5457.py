n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
n4 = float(input("n4: "))
media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
	print(round(media,2))
	print("Aprovado")
else:
	print(round(media, 2))
	print("Reprovado")
