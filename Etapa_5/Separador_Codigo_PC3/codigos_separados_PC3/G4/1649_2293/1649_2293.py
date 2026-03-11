from numpy import* 
s = input("").lower()
vet = s.split(',')
o = zeros(5, dtype=int) 
for i in vet:
	if i == 'p':
		o[0] += 1
	elif i == 'c':
		o[1] += 1
	elif i == 'm':
		o[2] += 1
	elif i == 'v':
		o[3] += 1
	else:
		o[4] += 1
print(max(o))
print(o)
		