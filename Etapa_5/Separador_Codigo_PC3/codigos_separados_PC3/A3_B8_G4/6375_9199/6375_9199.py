from numpy import *

votos = input("digite:").split(',')
v = zeros(4, dtype=int)
qnt = 0
cont = 0

for i in range(size(votos)):
	if votos[i] == "A":
		v[0] = v[0] + 1
	elif votos[i] == "B":
		v[1] = v[1] + 1
	elif votos[i] == "C":
		v[2] = v[2] + 1
	elif votos[i] == "D":
		v[3] = v[3] + 1

print(v)