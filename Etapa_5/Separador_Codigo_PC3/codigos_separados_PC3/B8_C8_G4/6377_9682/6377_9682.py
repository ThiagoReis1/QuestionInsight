from numpy import *
g = input().upper().split(",")
aux = zeros(4,dtype=int)
for i in range(0, len(g)):
	if g[i] == 'A':
		aux[0] += 1
	elif g[i] == 'B':
		aux[1] += 1
	elif g[i] == 'C':
		aux[2] += 1
	elif g[i] == 'D':
		aux[3] += 1
	i += 1
print(aux)