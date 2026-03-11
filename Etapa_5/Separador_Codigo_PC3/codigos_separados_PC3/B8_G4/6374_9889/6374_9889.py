from numpy import *

p = input("Digite 'O' para oftalmo, 'D' para dermato, 'N' para neuro e 'C' para cardio: ").upper().split(',')

qpa = zeros(4, dtype = int)

for i in p:
	if (i == 'O'):
		qpa[0] = qpa[0] + 1
		
	elif (i == 'D'):
		qpa[1] = qpa[1] + 1
		
	elif (i == 'N'):
		qpa[2] = qpa[2] + 1
		
	elif (i == 'C'):
		qpa[3] = qpa[3] + 1
		
print(qpa)