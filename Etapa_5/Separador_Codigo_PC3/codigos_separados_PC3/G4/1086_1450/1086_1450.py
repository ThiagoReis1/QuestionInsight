# Universidade Federal do Amazonas
# Aluna: Karina Rocha Ferreira - 21554907
# Avaliacao 2. 29/06/2016

p1 = float(input())
p2 = float(input())
p3 = float(input())

media = (p1 + p2 + p3)/ 3

if (media >= 7):
	print(round(media,1))
	print("Aprovado")
else:
	print(round(media,1))
	print("Reprovado")