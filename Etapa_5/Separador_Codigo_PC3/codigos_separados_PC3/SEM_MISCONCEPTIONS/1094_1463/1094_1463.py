#Ingrid do Nascimento Mendes
#30/06/2016

numero = input()

c1 = int(numero[0]) * 100
d1 = int(numero[1]) * 10
u1 = int(numero[2])

parte1 = c1 + d1 + u1

c2 = int(numero[3]) * 100
d2 = int(numero[4]) * 10
u2 = int(numero[5])

numero = int(numero)

parte2 = c2 + d2 + u2

propriedade = (parte1 + parte2) ** 2

if (propriedade==numero):
	print(numero,"atende a propriedade")
else:
	print(propriedade)
