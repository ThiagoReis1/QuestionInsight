from numpy import *

notas = array(eval(input()))

soma = sum(notas) - min(notas)

print(round(soma / (size(notas) - 1), 2))