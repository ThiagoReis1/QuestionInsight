N = int(input("numero inteiro: "))

if(N>=1) :
	if(N % 3 == 0) and (N % 5 ==0) :
		print("TicTac")
	elif(N % 5 == 0):
		print("Tac")
	elif(N % 3 == 0) :
		print("Tic")
	else:
		print("N")
else:
	print("N")
  