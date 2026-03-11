from numpy import*
notas = array(eval(input()))
pesos = array([4,3])
i = 0
media = 0

while i < size(pesos):
	media = media + (notas[i] * pesos[i] / 7)
	i = i + 1
print(round(media, 2))

