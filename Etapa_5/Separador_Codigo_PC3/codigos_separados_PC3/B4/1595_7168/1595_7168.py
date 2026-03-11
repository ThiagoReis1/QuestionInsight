from numpy import *

notas = array(eval(input("notas: ")))
i=0

if notas[i] == min(notas):
	media = sum(notas)/ size(notas)
	print(round(media,2))
else:
	media= sum(notas)/ size(notas)
	print(round(media,2))