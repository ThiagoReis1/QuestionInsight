from numpy import array
vec = input().split(',')
contadores = array([0,0,0,0,0])
for i in vec:
	if i == 'A':
		contadores[0] += 1
	elif i == 'B':
		contadores[1] += 1
	elif i == 'C':
		contadores[2] += 1
	elif i == 'D':
		contadores[3] += 1
	elif i == 'E':
		contadores[4] += 1
print(contadores)