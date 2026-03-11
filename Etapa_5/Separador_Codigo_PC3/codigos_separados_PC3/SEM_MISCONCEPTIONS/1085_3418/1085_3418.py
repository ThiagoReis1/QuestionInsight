#ENTRADA

from math import*

notas_obtidas1 = float(input("Nota 1: "))
notas_obtidas2 = float(input("Nota 2: "))
notas_obtidas3 = float(input("Nota 3: "))
notas_obtidas4 = float(input("Nota 4: "))
notas_obtidas5 = float(input("Nota 5: "))

#CONVERSAO

media_aritmetica = (notas_obtidas1 + notas_obtidas2 + notas_obtidas3 + notas_obtidas4 + notas_obtidas5)/ 5

if (media_aritmetica >= 6.0):
	print((round(media_aritmetica, 2)),"Aprovacao")
else:
	print((round(media_aritmetica, 2)),"Reprovacao")
	
#FIM