from numpy import*

v = input("vetor:").split(',')
cont = zeros(5, dtype=int)
mr = 0

for i in range(size(v)):
	if v[i] == 'AC':
		cont[0] += 1
	if v[i] == 'AM':
		cont[1] += 1
	if v[i] == 'PA':
		cont[2] += 1
	if v[i] == 'RO':
		cont[3] += 1
	if v[i] == 'RR':
		cont[4] += 1

for i in cont:
	if i > mr:
		mr = i
print(mr)
print(cont)
	

