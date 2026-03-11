from numpy import*
turma = array(eval(input("")))
a = 0

for i in range (size(turma)):
	if turma[i] / 5 == 0:
		a += 1
	ind = zeros(a,dtype = int)
print(i)
j = 0
for i in range(size(turma)):
	if turma[i] / 5 == 0:
		ind[j] = i
		j += 1
print(ind)