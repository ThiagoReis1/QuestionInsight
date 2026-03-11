from numpy import*

vet = array(input("digite os tons:").split(','))
aux = zeros(6, dtype=int)

for i in vet:
	if i == "MC":
		aux[0] = aux[0] + 1
	elif i == "C":
		aux[1] = aux[1] + 1
	elif i == "CM":
		aux[2] = aux[2] + 1
	elif i == "EM":
		aux[3] = aux[3] + 1
	elif i == "E":
		aux[4] = aux[4] + 1
	elif i == "ME":
		aux[5] = aux[4] + 1

print(max(aux))
print(aux)