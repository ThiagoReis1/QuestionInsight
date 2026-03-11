prova_1 = float(input("Nota: "))
prova_2 = float(input("Nota: "))
prova_3 = float(input("Nota: "))

media = (prova_1 + prova_2 + prova_3) / 3

if (media >= 5):
	print(round(media, 1))
	print("Aprovado")

else:
	print(round(media, 1))
	print("Reprovado")
