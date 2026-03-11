from numpy import *

nota = array(eval(input("calcular media")))
peso = array([5, 1])

num = sum(nota * peso) 
den = sum(peso)

media = num / den
print(round(media, 2))

