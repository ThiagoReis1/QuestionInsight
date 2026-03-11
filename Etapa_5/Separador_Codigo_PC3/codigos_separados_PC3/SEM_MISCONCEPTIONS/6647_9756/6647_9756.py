from numpy import *

pesos = array([2,1,5])
notas = array(eval(input("Insira as notas: ")))

notas = notas * pesos
somnotas = sum(notas)
sompesos = sum(pesos)

mpon = somnotas/sompesos

print (round(mpon, 2))