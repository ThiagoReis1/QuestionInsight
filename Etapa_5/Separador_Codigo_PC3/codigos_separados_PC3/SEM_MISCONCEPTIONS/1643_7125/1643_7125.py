from numpy import *

notas = array(eval(input("notas: ")))


cont = 0

for x in range(size(notas)):
	if notas[x] >= 5:
		cont = cont + 1
print(cont)

media = zeros(cont, dtype = int)
j = 0

for x in range(size(notas)):
	if notas[x] >= 5:
		media[j] = x
		j = j + 1
print(media)





