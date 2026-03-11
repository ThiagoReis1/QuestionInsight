from numpy import *
from numpy.linalg import *

turmas = array(eval(input("valor: ")))

qnt = 0
for ele in turmas:
	if ele%5 == 0:
		qnt += 1
		
turmas2 = zeros(qnt, dtype=int) 	
qnt = 0
for i in range(len(turmas)):
	if turmas[i]%5 == 0:
		turmas2[qnt] = i
		qnt +=1
print(qnt)
print(turmas2)