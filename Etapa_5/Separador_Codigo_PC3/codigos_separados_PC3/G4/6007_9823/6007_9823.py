qe = int(input())

if qe >= 6:
	e = 1.50
	t = qe*e
	print(round(t,2))
else:
	e = 1.85
	t = qe*e
	print(round(t,2))