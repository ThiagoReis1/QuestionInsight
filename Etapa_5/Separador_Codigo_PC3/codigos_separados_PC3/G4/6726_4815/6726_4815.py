num = int(input())

if num % 29 == 0:
	print(num // 29)
	print("sim")
else:
	print(num % 29)
	print("nao")