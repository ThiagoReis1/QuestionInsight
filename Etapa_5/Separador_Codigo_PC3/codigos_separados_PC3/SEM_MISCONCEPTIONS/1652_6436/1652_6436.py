from numpy import*

x = input("").split(',')
cont = zeros(5, dtype = int)
maior = 0
for i in range(size(x)):
	if x[i] == 'B':
		cont[0] += 1
	if x[i] == 'PA':
		cont[1] += 1
	if x[i] == 'PR':
		cont[2] += 1
	if x[i] == 'A':
		cont[3] += 1
	if x[i] == 'I':
		cont[4] += 1
		
for i in cont:
	if i > maior:
		maior = i
print(maior)
print(cont)