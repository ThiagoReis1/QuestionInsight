from numpy import*

et = input(": ").split(",")

cont = zeros(5, dtype = int)

for i in et:
	if i == 'B':
		cont[0] = cont[0] + 1
	elif i == 'PA':
		cont[1] = cont [1] + 1
	elif i == 'PR':
		cont[2] = cont[2] + 1
	elif i == 'A':
		cont[3] = cont[3] + 1
	elif i == 'I':
		cont[4] = cont[4] + 1

print(max(cont))

print(cont)
