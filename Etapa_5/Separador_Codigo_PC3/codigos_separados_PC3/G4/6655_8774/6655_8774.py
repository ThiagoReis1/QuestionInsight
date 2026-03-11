from numpy import *

nota = array(eval(input()))
peso = array([5, 1])

soma = sum(nota * peso) / sum(peso)
print(round(soma, 2))