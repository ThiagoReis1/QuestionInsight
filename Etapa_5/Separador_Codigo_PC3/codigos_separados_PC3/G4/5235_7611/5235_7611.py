n = int(input(''))
if n >= 1:
	n3 = n%3
	n5 = n%5
	if n3 == 0 and n5 != 0:
		print('Plunct')
	elif n5 == 0 and n3 != 0:
		print('Plact')
	elif n3 == 0 and n5 == 0:
		print('Zuuum')
	else:
		print(n)
else:
	print(n)