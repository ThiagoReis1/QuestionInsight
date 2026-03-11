n = int(input())
p = input().upper()

if p == 'B':
	i = 2023 - n
	if i >= 21:
		print("sim")
		a = i - 21
		print(a)
	else:
		print("nao")
		a = 21 - i
		print(a)
elif p == 'E':
	i = 2023 - n
	if i >= 18:
		print("sim")
		a = i - 18
		print(a)
	else:
		print("nao")
		a = 18 - i
		print(a)
else:
	print("invalido")