from numpy import *

notas = array(eval(input("digite as notas")))
media = 0
for i in range(size(notas)):
	media = media + (i+1)*notas[i]
d = 0
for i in range(size(notas)):
	d = d + (i+1)
media = media/d
print(round(media,2))