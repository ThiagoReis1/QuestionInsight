N=int(input("insira um numero:"))

if (N>=1):
	if(N%3 == 0 and N%5 == 0):
	   print("TicTac")
	elif (N%3 == 0 and N%5!=0):
		print("Tic")
	elif (N%5 == 0 and N%3!=0):
		print("Tac")
	else:
		print(N)
else:
	print(N)
