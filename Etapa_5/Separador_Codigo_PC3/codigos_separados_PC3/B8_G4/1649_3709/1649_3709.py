from numpy import*
s = input().split(',')
c1 = 0
vet = zeros(5, dtype=int)
while c1 < len(s):
	if (s[c1].upper() == 'P'):
		vet[0] += 1
	elif (s[c1].upper() == 'C'):
		vet[1] += 1
	elif (s[c1].upper() == 'M'):
		vet[2] += 1
	elif (s[c1].upper() == 'V'):
		vet[3] += 1
	elif (s[c1].upper() == 'A'):
		vet[4] += 1
	c1 += 1
print(max(vet))
print(vet)