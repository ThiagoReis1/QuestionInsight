x = int(input('digite o valor x: '))
y = int(input('digite o valor y: '))

i = x
cont = 0

while i <= y:
	if i % 2 != 0:
		print(i)
	i += 1
	