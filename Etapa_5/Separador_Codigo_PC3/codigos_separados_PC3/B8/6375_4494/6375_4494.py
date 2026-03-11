from numpy import *

votos = input().split(",")
results = zeros(4, dtype=int)

for i in range(size(votos)):
	if votos[i] == "A":
		results[0] += 1
	elif votos[i] == "B":
		results[1] += 1
	elif votos[i] == "C":
		results[2] += 1
	elif votos[i] == "D":
		results[3] += 1

print(results)