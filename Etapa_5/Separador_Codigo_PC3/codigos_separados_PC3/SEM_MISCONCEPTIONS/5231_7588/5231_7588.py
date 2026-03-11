numInt = int(input())


if((numInt % 3) == 0) and ((numInt % 5) == 0):
	print('FizzBuzz')
elif((numInt % 3) == 0):
	print('Fizz')
elif((numInt % 5) == 0):
	print('Buzz')

else:
	print(numInt)