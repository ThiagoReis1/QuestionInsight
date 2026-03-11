n = int(input("Digite o numero inteiro: "))

if n >=1 :
	if (n % 3 == 0) and (n % 5 == 0) :
		print ("TicTac")
	else:
		if (n % 3 == 0) :
			print("Tic")
		else:
			if (n % 5 == 0) :
				print("Tac")	
			else:
				print(n)