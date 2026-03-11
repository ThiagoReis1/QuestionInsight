from numpy import*
alunos = array(eval(input("")))
acu = 0
for i in (alunos):
	if i % 3 == 0:
		acu += 1
print(acu)

p = zeros(acu, dtype = int)
j = 0
for i in size(alunos):
	if p[i]%3 == 0:
		p[j] = i
	j += 1
print(p)