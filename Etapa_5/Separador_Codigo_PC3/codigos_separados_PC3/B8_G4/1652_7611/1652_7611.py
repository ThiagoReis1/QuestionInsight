from numpy import*

b = 0
pa = 0
pr = 0
a = 0
I = 0

e = (input('').upper()).split(',')
v = zeros(5, dtype = int)
for i in range(len(e)):
	if e[i] == 'B':
		b += 1
	elif e[i] == 'PA':
		pa += 1
	elif e[i] == 'PR':
		pr += 1
	elif e[i] == 'A':
		a += 1
	elif e[i] == 'I':
		I += 1
v[0] = b
v[1] = pa
v[2] = pr
v[3] = a
v[4] = I
print(max(v))
print(v)