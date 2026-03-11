num = int(input('numeoro: '))

cont = 0

while num != -1:
	if 45 <= num <= 150:
		cont += 1
	num = int(input('digite o numero: '))
print(cont)