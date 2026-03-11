from math import*
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
nota5 = float(input("Nota 5: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(round(media, 1))

if media >= 5.0:
	print("Aprovado")
else:
	print("Reprovado")