nota1 = float(input("insira a p1: "))
nota2 = float(input("insira a p2: "))
nota3 = float(input("insira a p3: "))
nota4 = float(input("insira a p4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
	print(round(media, 2))
	print("Aprovado")
else:
	print(round(media, 2))
	print("Reprovado")
