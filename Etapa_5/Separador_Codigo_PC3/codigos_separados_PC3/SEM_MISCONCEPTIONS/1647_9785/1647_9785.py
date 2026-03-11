from numpy import*

turmas = array(eval(input('')))
inteiro = 0

for i in range(size(turmas)):
	if turmas[i] >=70:
		inteiro +=1
ind= zeros (inteiro, dtype=int)
j = 0
for i in range(size(turmas)):
	if turmas[i] >=70:
		ind[j] = i
		j+= 1
print(inteiro)

j = 0

for i in range(size(turmas)):
	if turmas[i] >=70:
		ind[j] = i
		j += 1
print(ind)