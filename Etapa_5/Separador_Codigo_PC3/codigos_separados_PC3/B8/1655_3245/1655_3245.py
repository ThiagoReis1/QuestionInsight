from numpy import *

s = input().split(',')

contAC = 0
contAM = 0
contPA = 0
contRO = 0
contRR = 0

for i in range(len(s)):
	if(s[i] == 'AC'):
		contAC = contAC + 1
	elif (s[i] == 'AM'):
		contAM = contAM + 1
	elif (s[i] == 'PA'):
		contPA = contPA + 1
	elif (s[i] == 'RO'):
		contRO = contRO + 1
	elif (s[i] == 'RR'):
		contRR = contRR + 1	

v = zeros(5, dtype=int)		

v[0] = contAC
v[1] = contAM
v[2] = contPA
v[3] = contRO
v[4] = contRR

print(max(v))
print(v)
