from numpy import*

turmas = array(eval(input('')))
impar = 0

for i in range(size(turmas)):
	if turmas[i] % 2 != 0:
		impar +=1
ind= zeros (impar, dtype= int)
j = 0
for i in range(size(turmas)):
	if turmas[i] % 2 != 0:
		ind[j] = i
		j+= 1
print(impar)
print(ind)