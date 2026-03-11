N = int(input("Numero Inteiro: "))

if((N % 3 == 0) or (N % 5 == 0)):
	if(N % 3 == 0 and N % 5 ==0):
		print("AuauMiau")
	elif( N % 3 == 0 and not (N % 5 == 0 )):
		print("Auau")
	elif(N % 5 == 0 and not (N % 3 == 0)):
		print("Miau")
else: 
	print(N)