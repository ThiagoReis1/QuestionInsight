from numpy import*
vet = input().upper().split(',')
s = zeros(4, dtype=int)
for i in range(len(vet)):
	if vet[i] == 'A':
		s[0] += 1
	elif vet[i] == 'B':
		s[1] += 1
	elif vet[i] == 'C':
		s[2] += 1
	elif vet[i] == 'D':
		s[3] += 1
print(s)