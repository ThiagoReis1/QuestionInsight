x = input()
qt = int(input())
ac = int(input())

if x.upper() == "T":
	total = (4.50*qt)+(ac*12.00)
	print(round(total,2))

else:
	total = (5.00*qt)+(ac*12.00)
	print(round(total,2))
