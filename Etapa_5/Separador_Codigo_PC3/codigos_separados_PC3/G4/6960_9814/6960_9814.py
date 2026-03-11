x = int(input('Determine o valor do intervalo: '))
y = int(input('Determine o valor do intervalo: '))

i = x

while i <= y:
	if i % 2 != 0:
		print(i)
	i += 1