n = int(input())

if n % 13 == 0:
	print(n//13)
	print("sim")
else:
	print(n%13)
	print("nao")