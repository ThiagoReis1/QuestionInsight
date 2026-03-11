x=float(input("N:"))
if(x>=1):
	if(x%5==0 and(not x%3==0)):
		print("Buzz")
	elif(x%3==0 and(not x%5==0)):
		print("Fizz")
	elif(x%5==0 and x%3==0):
		print("FizzBuzz")
	else:
		print(x)