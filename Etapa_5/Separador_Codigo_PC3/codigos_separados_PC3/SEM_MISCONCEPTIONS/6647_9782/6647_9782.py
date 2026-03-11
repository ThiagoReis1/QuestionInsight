from numpy import *

notas = array(eval(input("Insira as 3 notas: ")))
peso = array([2, 1, 5])

numero = notas * peso
media = sum(numero) / sum(peso)
print(round(media, 2))

