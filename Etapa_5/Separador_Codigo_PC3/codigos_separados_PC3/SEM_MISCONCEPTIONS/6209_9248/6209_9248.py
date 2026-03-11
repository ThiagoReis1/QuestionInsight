N = int(input('digite o numero: '))
count = 0
while (N != -1):
	if (N >= 76) and (N <= 100):
		count = count + 1
	N = int(input('numero: '))
print(count)