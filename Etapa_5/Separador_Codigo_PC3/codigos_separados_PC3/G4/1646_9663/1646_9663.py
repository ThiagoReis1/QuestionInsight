from numpy import*

vetor = array(eval(input()))
cont = 0


for i in range(0, size(vetor)):
	if vetor[i] <= 50:
		cont+= 1
			
print(cont)
v = zeros(cont, dtype = int)
j = 0
for i in range(0, size(vetor)):
	if vetor[i] <= 50:
		v[j] = i
		j = j + 1
print(v)
	