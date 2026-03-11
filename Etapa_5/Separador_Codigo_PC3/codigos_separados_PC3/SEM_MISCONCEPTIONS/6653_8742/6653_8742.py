from numpy import*
nota = array(eval(input("notas: ")))
peso = [3,5,1]
desgraca = zeros(size(nota), dtype=int)
i = 0


while i < size(nota):
	desgraca[i] = nota[i] * peso[i]

	i = i + 1
media = sum(desgraca)/sum(peso)
print(round(media, 2))