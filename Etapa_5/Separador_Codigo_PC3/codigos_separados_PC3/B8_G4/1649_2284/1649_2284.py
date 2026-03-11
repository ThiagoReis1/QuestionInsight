from numpy import*

s = input("Cor dos olhos: ")

v = zeros(5, dtype = int)

for i in s:
	if (i == 'P'):
		v[0] += 1
	elif (i == 'C'):
		v[1] += 1
	elif (i == 'M'):
		v[2] += 1
	elif (i == 'V'):
		v[3] += 1
	elif (i == 'A'):
		v[4] += 1

print(max(v))
print(v)