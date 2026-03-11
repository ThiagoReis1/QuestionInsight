from numpy import *

turma = array(eval(input("turmas: ")))
c = 0
count = 0
for i in turma:
	if i%3 == 0:
		c += 1
trio = zeros(c, dtype = 'int')

for i in range(size(turma)):
	if turma[i]%3 == 0:
		trio[count] += i
		count +=1
		
print(c)
print(trio)