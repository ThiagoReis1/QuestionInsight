x = int(input())

if x%37 == 0:
	t = x//37
	print(t)
	print("sim")
else:
	t = x%37
	print(t)
	print("nao")