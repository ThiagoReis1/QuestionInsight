# Talita Passos
# Matricula - 21552161
# 30 de Junho de 2016
# Avaliacao 2 - Ex 1

prova1 = float(input("Digite a nota da p1: "))
prova2 = float(input("Digite a nota da p2: "))
prova3 = float(input("Digite a nota da p3: "))

media = (prova1 + prova2 + prova3) / 3

if(media >= 7):
	print(round(media, 1))
	print("Aprovado")
else:
	print(round(media, 1))
	print("Reprovado")