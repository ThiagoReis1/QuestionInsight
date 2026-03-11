N = int(input())


if (N%3 == 0 and N%5 != 0):
	print("Plunct")
elif (N%5 == 0 and N%3 != 0):
	print("Plact")
elif(N%3 == 0 and N%5 == 0):
	print("Zuuum")
elif(N%3 != 0 or N%5 != 0):
	print(N)
	