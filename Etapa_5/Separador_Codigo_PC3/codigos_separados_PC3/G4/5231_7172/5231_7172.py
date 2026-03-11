x=int(input("x: "))

if(x>=1):
	if(x%3==0 and x%5==0):
		print("FizzBuzz")
	elif(x%3==0 and x%5!=0):
		print("Fizz")
	elif(x%3!=0 and x%5==0):
		print("Buzz")
	else:
		print(x)