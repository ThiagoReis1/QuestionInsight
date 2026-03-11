a = int(input("num: "))
if((a>=1)and(a%3==0)and(a%5==0)):
	print("FizzBuzz")
elif((a>=1)and(a%5==0)):
	print("Buzz")
elif((a>=1)and(a%3==0)):
	print("Fizz")
else:
	print(a)
	
	