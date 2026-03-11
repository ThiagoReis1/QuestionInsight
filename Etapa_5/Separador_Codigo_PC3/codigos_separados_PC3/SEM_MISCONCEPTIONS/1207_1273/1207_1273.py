from numpy import *

dist = array(eval(input("Entre com as distancias dos lancamentos: ")))

recorde = 98.48


k = 0
i = 0
while (i < size(dist)):
	if (dist[i] > recorde):
		k = k + 1
		i = i + 1
	else:
		i = i + 1
		
dist_recorde = array(zeros(k, dtype = float))

i = 0
j = 0
while (i < size(dist)):
	if (dist[i] > recorde):
		dist_recorde[j] = dist[i]
		i = i + 1
		j = j + 1
	else:
		i = i + 1
print(recorde)
print(k)
		
