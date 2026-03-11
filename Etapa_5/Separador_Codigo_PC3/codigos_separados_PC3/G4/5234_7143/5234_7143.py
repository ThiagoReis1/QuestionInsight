n = int(input("Digite o numero: "))

if (n >= 1):
	if(((n % 3 )== 0) and ((n % 5)==0)):
		print("TicTac")
	elif ((n % 3) == 0):
		print("Tic")
	elif ((n % 5) == 0):
		print("Tac")
	else:
		print ( n )
	