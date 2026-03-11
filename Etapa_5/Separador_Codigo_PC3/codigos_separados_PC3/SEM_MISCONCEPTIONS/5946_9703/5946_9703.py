lanche = input()
qt =  int(input())
refri = int(input())

if lanche.upper() == "L":
	total = qt * 6 + refri * 3
	print(round(total, 2))
else:
	total = qt * 4.5 + refri * 3
	print(round(total, 2))
	