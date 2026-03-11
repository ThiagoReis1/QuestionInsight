num = int(input('Forneca um numero: '))
d1 = (num // 100)
d2 = (num % 100)
calc = (d1 ** 2) + (d2 ** 2)

if (calc == num):
	print('atende')
	print(num)
	
else: 
	print('nao atende')
	print(num)
	
