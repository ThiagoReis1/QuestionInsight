n = int(input("n: "))

g = n%3
a = n%5

if(n>=1):
	if(g==0) and (a==0):
		print("FizzBuzz")
	
	elif(g==0):
		print("Fizz")
	
	elif(a==0):
		print("Buzz")
		
	else: 
		print(n)