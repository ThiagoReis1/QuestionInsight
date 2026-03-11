x = int(input())
if x % 43 == 0:
	q = x // 43
	print(q)
	print("sim")
else:
	r = x % 43
	print(r)
	print("nao")
