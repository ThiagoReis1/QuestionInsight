from numpy import *

notas = array(eval(input()))

media = (4*notas[0]+3*notas[1])/7

print(round(media, 2))