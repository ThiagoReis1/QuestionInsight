#Universidade Federal do Amazonas
#Marcos Stephano Maia de Lima - 21602344
#14 / 07 / 2016

from math import*
na = float(input("Nota 1: "))
nb = float(input("Nota 2: "))
nc = float(input("Nota 3: "))
nd = float(input("Nota 4: "))
ne = float(input("Nota 5: "))

media = (na + nb + nc + nd + ne) // 5
print(media, 2)
if (media >= 6):
		print("Aprovado")
else:
		print ("Reprovado")
