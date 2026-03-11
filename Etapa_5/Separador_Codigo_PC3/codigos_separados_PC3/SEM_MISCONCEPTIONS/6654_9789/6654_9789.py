from numpy import *

nota = array(eval(input()))
peso = array([1,3,2,5])
numero = nota * peso
media = sum(numero)/ sum (peso)
print(round(media, 2))