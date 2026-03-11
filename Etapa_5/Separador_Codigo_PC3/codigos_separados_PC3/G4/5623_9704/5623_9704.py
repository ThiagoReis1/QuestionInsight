fb = input()
qt = int(input())
cap = int(input())

if fb.upper() == "B":
	t = qt * 5 + cap * 7.5
	print(round(t, 2))
else:
	t = qt * 4 + cap * 7.5
	print(round(t, 2))