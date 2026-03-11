###########################
#
# Paulo Sergio da Silva Freitas
# Avaliação Parcial 02
# Programa: Calculo de Médias
###############################
import math
nota1 = round(float(input("Informe a nota 1 :")),1)
nota2 = round(float(input("Informe a nota 1 :")),1)
nota3 = round(float(input("Informe a nota 1 :")),1)
media = (nota1+nota2+nota3)/3
print(round(media,1))
if (media >= 7):
	print("Aprovado")
else:
	print("Reprovado")