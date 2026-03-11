# Letícia Filardi - 21601147
# Avaliação 02

p1 = float (input ("Prova 1:"))
p2 = float (input ("Prova 2:"))
p3 = float (input ("Prova 3:"))

media = (p1 + p2 + p3)/3

if (media >= 7):
	print (round (media, 1))
	print ("Aprovado")
else:
	print (round (media, 1))
	print ("Reprovado")