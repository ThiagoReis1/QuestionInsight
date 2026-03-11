a = int(input(''))
n = a // 1000
p = a % 1000

if ((n - p)**2 == a):
	print('atende')
	print(a)
else:
   print('nao atende')
   print(a)
