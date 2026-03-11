from numpy import*

v = zeros(6, dtype=int)
vet = input(" ").upper().split(',')

for i in range(size(vet)):
	if (vet[i] == 'MC'):
		v[0] = v[0] + 1
	elif (vet[i] == 'C'):
		v[1] = v[1] + 1
	elif (vet[i] == 'CM'):
		v[2] = v[2] + 1
	elif (vet[i] == 'EM'):
		v[3] = v[3] + 1
	elif (vet[i] == 'E'):
		v[4] = v[4] + 1
	elif (vet[i] == 'ME'):
		v[5] = v[5] + 1
print(max(v))
print(v)
