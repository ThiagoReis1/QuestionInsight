n = int(input("numero: "))

a = n%3
b = n%5

if a == 0 and b != 0:
	print("Tic")
	
elif a != 0 and b == 0:
	print("Tac")
	
elif a == 0 and b == 0:
	print("TicTac")
	
else:
	print(n)
	  