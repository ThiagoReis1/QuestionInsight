num = int(input("digite o numero: "))

if (num >= 1):
	if (num % 3) == 0 and (num % 5) == 0:
		print("TicTac")
	elif (num % 5) == 0:
		print("Tac")
	elif (num % 3) == 0:
		print("Tic")
	else:
		print(num)