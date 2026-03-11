N= int(input("digite o numero inteiro:"))

if (N % 3 == 0 and N % 5 == 0) :
	print("FizzBuzz")
elif (N % 3 == 0) :
	print("Fizz")
else:
	N= (N % 5 == 0)
	print("Buzz")
print(N)