from numpy import *

notas = array(eval(input("Digite as notas: ")))

valores = 0

for i in range (size(notas)):
	if notas[i] >= 70:
		valores += 1

vetor = zeros(valores, dtype = int)

b = 0

for i in range (size(notas)):
	if notas[i] >= 70:
		vetor[b] = i
		b += 1

print(b)
print(vetor)