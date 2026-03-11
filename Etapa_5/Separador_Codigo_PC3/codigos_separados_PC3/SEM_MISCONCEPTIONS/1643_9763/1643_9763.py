from numpy import*

notas = array(eval(input("informe as notas: ")))
c = 0
for i in range(0, size(notas)):
	if notas[i] >= 5:
		c = c + 1
print(c)

vetor = zeros(c,dtype=int)
j = 0
for i in range(0, size(notas)):
	if notas[i] >= 5:
		vetor[j] = i
		j = j + 1
print(vetor)
	
	