num = int(input('digite o numero inteiro: '))

cal = num // 17 
if num % 17 == 0:
	print(cal)
	print('sim')
	
else:
	print(num % 17)
	print('nao')
