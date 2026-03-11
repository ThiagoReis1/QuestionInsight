num = int(input())

if num%3 == 0 and num%5==0:
	print('TicTac')
elif num%3 == 0:
	print('Tic')
elif num%5 == 0:
	print('Tac')
else:
	print(num)