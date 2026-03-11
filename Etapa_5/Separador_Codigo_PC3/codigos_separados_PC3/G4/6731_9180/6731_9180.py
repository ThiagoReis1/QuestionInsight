num = int(input('Digite um numero:'))

if(num%47 == 0):
	print(num//47)
	print('sim')
else:
	print(num%47)
	print('nao')