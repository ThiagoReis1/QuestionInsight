N= int(input("Numero:"))

if(N>=1):
	if(N % 3 == 0 and N % 5 == 0):
		print("FizzBuzz")
	elif(N % 3 == 0):
		print("Fizz")
	elif(N % 5 == 0):
		print("Buzz")
	else:
		print(N)
else:
	print(N)