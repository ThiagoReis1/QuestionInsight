n= int(input(""))
nd1= n %3
nd2= n % 5

if n >= 1:
	if nd1 == 0 and nd2 == 0:
		print("FizzBuzz")
	elif nd2 == 0:
		print("Buzz")
	elif nd1 == 0 :
		print("Fizz")
	else:
		print(n)
else: 
	print(n)
	