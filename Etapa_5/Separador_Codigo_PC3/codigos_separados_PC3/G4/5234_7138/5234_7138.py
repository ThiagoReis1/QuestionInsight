n = int(input())

if(n >= 1):
	if(n%3 == 0 and n%5 == 0):
		print("TicTac")
	elif(n%5 == 0):
		print("Tac")
	elif(n%3 == 0):
		print("Tic")
	else:
		print(n)
else:
	print(n)