q = int(input())
p = 30

if q < 10:
	c = p + 3.25
	print(round(c,2))
if q == 10:
	c = p + 4.50
	print(round(c,2))
if q > 10:
	c = p + 6
	print(round(c,2))