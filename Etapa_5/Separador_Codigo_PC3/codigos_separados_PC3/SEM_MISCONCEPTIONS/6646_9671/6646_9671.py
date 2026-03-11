from numpy import *

notas = array(eval(input("insira as tres notas: ")))
peso = array([1,2,3])

resultado = ((notas[0] * peso[0]) + (notas[1] * peso[1]) + (notas[2] * peso[2])) / sum(peso)
print(round(resultado, 2))