pesos = [5, 4, 3, 2]
notas = eval(input())

i = 0
media = 0
while i < len(pesos):
	media += pesos[i] * notas[i]
	i += 1

media = media / 14.0
print(round(media, 2))