from numpy import *

v = array(eval(input("vetor de notas")))

numerador = sum(v) - min(v)
denominador = size(v) - 1	
media = numerador / denominador

print(round(media, 2))
	
	
	