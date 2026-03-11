cons = float(input())
if(cons <= 100):
	const = cons * 1.20
	print (round(const, 2))
else:
	const = 25 + (cons * 1.40)
	print (round(const, 2))