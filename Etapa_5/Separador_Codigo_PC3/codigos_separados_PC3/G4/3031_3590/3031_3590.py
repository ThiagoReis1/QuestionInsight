N = float(input())

if (N <= 1):
	print("1")
elif (N <= 2):
	print("2")
elif (N <= 3):
	print(round(N ** 2,2))
else:
	print(round(N ** 3,2))