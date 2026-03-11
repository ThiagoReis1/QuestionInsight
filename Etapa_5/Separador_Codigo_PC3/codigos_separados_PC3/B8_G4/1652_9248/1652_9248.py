from numpy import *
s = input('n:').upper().split(',')
b = zeros(5, dtype = int)
for x in s:
	if x == 'B':
		b[0]  += 1
	elif x == 'PA':
		b[1] += 1
	elif x == 'PR':
		b[2] += 1
	elif x == 'A':
		b[3] += 1
	elif x == 'I':
		b[4] += 1
print(max(b))
print(b)