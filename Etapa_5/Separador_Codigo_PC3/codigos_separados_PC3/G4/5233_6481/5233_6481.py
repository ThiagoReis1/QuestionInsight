N = int(input())

if N >= 1:
	if (N % 3 == 0) and (N % 5 == 0):
		print('AuauMiau')
	else: 
		if (N % 3 == 0):
			print('Auau')
		elif (N % 5 == 0):
			print('Miau')
		else:
			print(N)