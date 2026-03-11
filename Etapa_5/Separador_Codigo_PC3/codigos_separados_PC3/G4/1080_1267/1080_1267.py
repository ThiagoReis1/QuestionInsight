from math import*

n1 = float(input("Digite a n1: "))
n2 = float(input("Digite a n2: "))
n3 = float(input("Digite a n3: "))

media = (n1 + n2 + n3) / 3

if(media >= 5):
	print(float(round(media, 1)))
	print("Aprovado")
else:
	print(float(round(media, 1)))
	print("Reprovado")