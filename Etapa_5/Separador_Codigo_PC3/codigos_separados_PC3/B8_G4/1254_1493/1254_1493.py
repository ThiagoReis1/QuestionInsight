#UNIVERSIDADE FEDERAL DO AMAZONAS
#ENGENHARIA QUIMICA
#MICHAEL EVANGELISTA DA CRUZ - 21600845

from numpy import *

v = array(eval(input("V: ")))

A = min(v)
B = max(v)
C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7 * B

vetor = array(zeros(2, dtype = int))

x1 = 0
x2 = 0

for i in v:	
	if i >= C and i < D:
		x1 = x1 + 1
	elif i >= D and i < B:
		x2 = x2 + 1	
		
	
	vetor[0] = x1
	vetor[1] = x2
	
print(vetor)
	