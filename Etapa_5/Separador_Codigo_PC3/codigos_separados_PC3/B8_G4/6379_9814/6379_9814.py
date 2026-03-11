from numpy import * 

s = input('Determine: ').upper().split(',')

v0 = zeros(5, dtype=int)

for i in s:
	if i == 'A':
		v0[0] += 1
	elif i == 'B':
		v0[1] += 1
	elif i == 'C':
		v0[2] += 1
	elif i == 'D':
		v0[3] += 1
	elif i == 'E':
		v0[4] += 1
	
print(v0)