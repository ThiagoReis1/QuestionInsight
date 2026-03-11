from numpy import*
a = input('nb').split(',')
b = zeros(5, dtype=int)
for i in a:
	if i == 'A':
		b[0] += 1
	elif i == 'B':
		b[1] += 1
	elif i == 'C':
		b[2] += 1
	elif i == 'D':
		b[3] += 1
	elif i == 'E':
		b[4] += 1
print(b)