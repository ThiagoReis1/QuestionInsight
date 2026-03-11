from numpy import *

notas = input('insira quais as notas').upper().split(',')
c = zeros(5,dtype=int)

for v in notas:
	if v =='A':
	   c[0] += 1
	elif v =='B':
		c[1] += 1
	elif v == 'C':
		c[2] += 1
	elif v == 'D':
		c[3] += 1
	elif v == 'E':
		c[4] += 1
print(c)