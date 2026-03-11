qnt_manga = int(input())

if (qnt_manga >= 6):
	total = qnt_manga * 3.45
	print(round(total, 2))
else:
	total = qnt_manga * 3.80
	print(round(total, 2))