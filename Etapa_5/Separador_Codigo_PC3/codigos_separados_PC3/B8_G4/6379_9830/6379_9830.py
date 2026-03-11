from numpy import *

nota = input("").upper().split(',')
cat = zeros(5, dtype=int)
for i in nota:
	if i == 'A':
		cat[0] += 1
	elif i == 'B':
		cat[1] += 1
	elif i == 'C':
		cat[2] += 1
	elif i == 'D':
		cat[3] += 1
	elif i == 'E':
		cat[4] += 1
		
print(cat)