N = int(input("digite o numero: "))

if (N % 3 == 0 or N % 5 == 0 or (N % 3 == 0 and N % 5 == 0)):
	if(N % 3 == 0 and N % 5 == 0):
		print("FizzBuzz")
	elif(N % 3 == 0):
		print("Fizz")
	elif(N % 5 == 0):
		print("Buzz")
			
else:
	print(N)

