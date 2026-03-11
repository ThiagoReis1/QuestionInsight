a = int(input(""))

if(a >= 1):
	if ( a%3 == 0 and a%5 == 0):
		x = "Zuuum"
		print(x)
	elif (a%5 == 0):
		x = "Plact"
		print(x)
	elif (a%3 == 0):
		x = "Plunct"
		print(x)
	else:
		print(a)