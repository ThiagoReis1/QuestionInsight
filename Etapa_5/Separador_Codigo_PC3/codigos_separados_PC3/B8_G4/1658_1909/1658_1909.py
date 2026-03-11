from numpy import* 

vet = input()
a = vet.split(',')
cont = zeros(5, dtype=int)

for i in range(size(a)):
	if (a[i] == 'CHN'):
		cont[0] = cont[0] + 1 
	elif (a[i] == 'JPN'):
		cont[1] = cont[1] + 1
	elif (a[i] == 'KOR'):
		cont[2] = cont[2] + 1
	elif (a[i] == 'MGL'):
		cont[3] = cont[3] + 1
	elif (a[i] == 'THA'):
		cont[4] = cont[4] + 1

print(max(cont))
print(cont)
		