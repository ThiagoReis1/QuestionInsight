from numpy import*
cont = zeros(4, dtype=int)
seq = input(": ").upper().split(',')
for i in range(size(seq)):
	if seq[i] == 'C':
		cont[0] = cont[0] + 1
	if seq[i] == 'D':
		cont[1] = cont[1] + 1
	if seq[i] == 'V':
		cont[2] = cont[2] + 1
	if seq[i] == 'U':
		cont[3] = cont[3] + 1
print(cont)