N= int(input())

if (N %3==0):
	print("Fizz")
elif (N%5==0):
	print("Buzz")
elif ((N%3==0) or (N%5==0)):	
	print("FizBuzz")
else:
	print(N)
	