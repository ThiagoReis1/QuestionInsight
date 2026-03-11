from numpy import *

v = array(eval(input("Informe a porcentagem das aulas frequentadas pelos alunos: ")))

acum = 0

for i in range(size(v)):
	if v[i]<70:
		acum = acum+1
		
print(acum)

v2 = zeros(acum,dtype=int)

j = 0
for i in range(size(v)):
	if v[i]<70:
		v2[j] = i
		j = j+1
		
print(v2)