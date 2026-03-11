n = int(input())

if n%3==0 and n%5==0:
	print("TicTac")
elif n%3==0:
	print("Tic")
elif  n%5==0:
	print("Tac")
elif n%3!=0 and n%5!=0:
	print(n)
