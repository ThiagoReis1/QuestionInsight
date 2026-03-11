from numpy import *

notas = array(eval(input("")))

soma = (notas[0] * 2) + (notas[1] * 1) + (notas[2] * 5)
    
media = soma /(2 + 1 + 5)

print(round(media, 2))