from numpy import*
s = input("").upper()
vet = s.split(',')
m = zeros(5, dtype=int)

for i in vet:
	if i == 'BE':
		m[0] += 1
	elif i == 'ES':
		m[1] += 1
	elif i == 'FR':
		m[2] += 1
	elif i == 'IT':
		m[3] += 1
	elif i == 'PT':
		m[4] += 1

print(max(m))
print(m)


