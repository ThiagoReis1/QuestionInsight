from numpy import *

notas = array(eval(input("Informe as notas: ")))
pesos = [4,3]

i = 0
media = 0

while i < size(pesos):
	media = media + notas[i]*pesos[i]
	
	i+=1
media = media / sum(pesos)

print(round(media,2))