N = int(input(': '))
if N%3 == 0 and N%5 !=0:
	print('Auau')
elif N%3 != 0 and N%5 == 0:
	print('Miau')
elif N%3 == 0 and N%5 == 0:
	print('AuauMiau')
else:
	print(N)