num = int(input('digite um numero:'))

if(num % 17 == 0):
		quociente = num // 17
		print(quociente,'sim')
else:
		resto = num % 17
		print(resto, 'nao')