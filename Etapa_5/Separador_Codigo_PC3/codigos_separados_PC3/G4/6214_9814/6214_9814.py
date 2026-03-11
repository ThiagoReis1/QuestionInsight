n = int(input('Determine o numero: '))

cont = 0

while n != -1:
	if 45 <= n <= 150:
		cont += 1
	n = int(input('determine o novo numero: '))
	
print(cont)