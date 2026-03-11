from numpy import*
g = array(eval(input(":")))
a = 0
for i in g:
	if(i % 2 != 0):
		a = a + 1
vetor = zeros(a, dtype = int)
j = 0
for i in g:
	if(i % 2 != 0):
		vetor[j] = vetor[j] + i
		j = j + 1
print(vetor)

