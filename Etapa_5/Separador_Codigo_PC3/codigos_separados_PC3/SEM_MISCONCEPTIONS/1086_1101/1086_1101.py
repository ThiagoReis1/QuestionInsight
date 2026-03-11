prova1 = float(input("Nota prova 1: "))
prova2 = float(input("Nota prova 2: "))
prova3 = float(input("Nota prova 3: "))

media = (prova1 + prova2 + prova3)/3
print(round(media, 1))

if (media >= 7.0):
	print("Aprovado")
else:
	print("Reprovado")